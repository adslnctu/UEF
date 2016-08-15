import sys, os
import datetime
import numpy
import math
import resource
import multiprocessing
import time
import pickle
sys.path.append('../../lib/fileDB/')
from fileDB import FileDB
sys.path.append('../../lib/featureHasher/')
from featureHasher import FeatureHasher
sys.path.append('../../lib/featureSelector/')
from significantFeatureSelector import SignificantFeatureSelector
sys.path.append('../../lib/classifier/')
from ssem import SSEM
from naiveBayesClassifier import NaiveBayesClassifier
def prepareDB(trainingFilenameList, testingFilenameList):
	trainingDBFilenameList=list()
	for filename in trainingFilenameList:
		trainingDBFilenameList.append("../../lib/fileDB/log/season2/"+filename)
	trainingDB=FileDB(trainingDBFilenameList)

	testingDBFilenameList=list()
	for filename in testingFilenameList:
		testingDBFilenameList.append("../../lib/fileDB/log/season2/"+filename)
	testingDB=FileDB(testingDBFilenameList)
	return trainingDB, testingDB
def prepareClassifier(beta0, decay, XSize):
	classifierList=[NaiveBayesClassifier(targetDimList=[i]) for i in range(XSize)]
	return SSEM(beta0=beta0, decay=decay, XSize=XSize, classifierList=classifierList)
def train(trainingDB, featureHasher, featureSelector, classifier):
	while True:
		try:
			x, y, currentTime=trainingDB.next()
			X=featureHasher.transform(x)
			Y=int(y)
			selectedX=featureSelector.transform(X)
			classifier.update(selectedX, Y)
		except StopIteration as stopIteration:
			break
def onlineRun(testingDB, featureHasher, featureSelector, classifier):
	while True:
		try:
			x, y, currentTime=testingDB.next()
			X=featureHasher.transform(x)
			Y=int(y)
			selectedX=featureSelector.transform(X)
			p=classifier.predict(selectedX)
			classifier.update(selectedX, Y)
		except StopIteration as stopIteration:
			break
def closeDB(trainingDB, testingDB):
	trainingDB.close()
	testingDB.close()
def run(beta0, selectSize, trainingDay, testingDay):
	decay=0.0
	trainingDB, testingDB=prepareDB([trainingDay+".log"], [testingDay+".log"])
	featureHasher=FeatureHasher(pow(2, 20))
	targetDimList=pickle.load(open("./targetDimList/season2/"+trainingDay+".pickle", "rb"))
	featureSelector=SignificantFeatureSelector(targetDimList=targetDimList[:selectSize])
	classifier=prepareClassifier(beta0=beta0, decay=decay, XSize=selectSize)
	train(trainingDB, featureHasher, featureSelector, classifier)
	#onlineRun(testingDB, featureHasher, featureSelector, classifier)
	file=open("./log/season2/"+testingDay+"/"+str(selectSize)+"_training.log", "w", 0)
	memory=float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)/1024
	file.write(str(memory))
	file.close()
	closeDB(trainingDB, testingDB)
def main():
	#for selectSize in [1, 20, 30, 40, 60, 80, 100]:
	#for selectSize in [200, 300]:
	for selectSize in [400, 500]:
		processList=list()
		dayList=["2013-06-06", "2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
		for i in range(len(dayList)-1):
			beta0=1.0
			dirname="./log/season2/"+dayList[i+1]+"/"
			if not os.path.isdir(dirname):
				os.mkdir(dirname)
			process=multiprocessing.Process(target=run, args=(beta0, selectSize, dayList[i], dayList[i+1]))
			process.start()
			processList.append(process)
			time.sleep(5)
		for process in processList:
			process.join()	
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
