import sys, os
import datetime
import numpy
import math
import multiprocessing
import time
sys.path.append('../../lib/fileDB/')
from fileDB import FileDB
sys.path.append('../../lib/featureHasher/')
from featureHasher import FeatureHasher
sys.path.append('../../lib/featureSelector/')
from significantFeatureSelector import SignificantFeatureSelector
sys.path.append('../../lib/classifier/')
from sem import SEM
from naiveBayesClassifier import NaiveBayesClassifier
def prepareDB(trainingFilenameList, testingFilenameList):
	trainingDBFilenameList=list()
	for filename in trainingFilenameList:
		trainingDBFilenameList.append("../../lib/fileDB/log/season3/"+filename)
	trainingDB=FileDB(trainingDBFilenameList)

	testingDBFilenameList=list()
	for filename in testingFilenameList:
		testingDBFilenameList.append("../../lib/fileDB/log/season3/"+filename)
	testingDB=FileDB(testingDBFilenameList)
	return trainingDB, testingDB
def prepareClassifier(beta0, decay, XSize):
	classifierList=[NaiveBayesClassifier(targetDimList=[i]) for i in range(XSize)]
	return SEM(beta0=beta0, decay=decay, XSize=XSize, classifierList=classifierList)
def train(trainingDB, featureHasher, featureSelector, classifier):
	lastShowTime=datetime.datetime.min
	while True:
		try:
			x, y, currentTime=trainingDB.next()
			X=featureHasher.transform(x)
			Y=int(y)
			selectedX=featureSelector.transform(X)
			classifier.update(selectedX, Y)
			if currentTime-lastShowTime>datetime.timedelta(minutes=60):
				print currentTime, "run at ", datetime.datetime.now()
				lastShowTime=currentTime
		except StopIteration as stopIteration:
			break
def onlineRun(testingDB, featureHasher, featureSelector, classifier, outFilename):
	file=open(outFilename, "w")
	while True:
		try:
			x, y, currentTime=testingDB.next()
			X=featureHasher.transform(x)
			Y=int(y)
			selectedX=featureSelector.transform(X)
			p=classifier.predict(selectedX)
			file.write(str(currentTime)+", "+str(Y==1)+", "+str(p)+"\n")
			classifier.update(selectedX, Y)
		except StopIteration as stopIteration:
			break
	file.close()
def closeDB(trainingDB, testingDB):
	trainingDB.close()
	testingDB.close()
def run(beta0, selectSize, trainingDay, testingDay):
	decay=0.0
	trainingDB, testingDB=prepareDB([trainingDay+".log"], [testingDay+".log"])
	featureHasher=FeatureHasher(pow(2, 20))
	featureSelector=SignificantFeatureSelector("../../lib/featureDistribution/pickle/season3/"+trainingDay+".pickle", selectSize=selectSize)
	classifier=prepareClassifier(beta0=beta0, decay=decay, XSize=selectSize)
	train(trainingDB, featureHasher, featureSelector, classifier)
	onlineRun(testingDB, featureHasher, featureSelector, classifier, "./log/season3/"+testingDay+"/"+str(beta0)+"_"+str(selectSize)+".log")
	closeDB(trainingDB, testingDB)
def main():
	dayList=["2013-10-19", "2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
	for i in range(len(dayList)-1):
		processList=list()
		for beta0 in [0.001, 0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]:
			#for selectSize in [1, 10, 20, 30, 40, 50]:
			for selectSize in [100]:
				dirname="./log/season3/"+dayList[i+1]+"/"
				if not os.path.isdir(dirname):
					os.mkdir(dirname)
				process=multiprocessing.Process(target=run, args=(beta0, selectSize, dayList[i], dayList[i+1]))
				process.start()
				processList.append(process)
				time.sleep(60)
		for process in processList:
			process.join()	
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
