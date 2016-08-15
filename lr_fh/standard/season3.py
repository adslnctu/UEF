import sys, os
import datetime
import numpy
import math
import pickle
from sklearn.linear_model import LogisticRegression
from scipy.sparse import vstack
sys.path.append('../../lib/fileDB/')
from fileDB import FileDB
sys.path.append('../../lib/featureHasher/')
from featureHasher import FeatureHasher
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
def prepareClassifier():
	return LogisticRegression()
def train(trainingDB, classifier, featureHasher):
	lastShowTime=datetime.datetime.min
	xList=list()
	yList=list()
	while True:
		try:
			x, y, currentTime=trainingDB.next()
			xList.append(x)
			yList.append(y)		
			if currentTime-lastShowTime>datetime.timedelta(hours=1):
				print currentTime, "run at ", datetime.datetime.now()
				lastShowTime=currentTime
		except StopIteration as stopIteration:
			break
	X=featureHasher.transformList(xList)
	Y=[int(y) for y in yList]
	classifier.fit(X, Y)
def onlineRun(testingDB, classifier, featureHasher, outFilename):
	file=open(outFilename, "w")
	while True:
		try:
			x, y, currentTime=testingDB.next()
			a=featureHasher.transform(x)
			p=classifier.predict_proba(a)[:, 1][0]
			file.write(str(y)+", "+str(p)+"\n")
		except StopIteration as stopIteration:
			break
	file.close()
def closeDB(trainingDB, testingDB):
	trainingDB.close()
	testingDB.close()
def run(trainingDay, testingDay):
	trainingDB, testingDB=prepareDB([trainingDay+".log"], [testingDay+".log"])
	classifier=prepareClassifier()
	featureHasher=FeatureHasher(pow(2, 18))
	train(trainingDB, classifier, featureHasher)
	onlineRun(testingDB, classifier, featureHasher, "./log/season3/"+testingDay+".log")
	closeDB(trainingDB, testingDB)
def main():
	dayList=["2013-10-19", "2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
	for i in range(len(dayList)-1):
		run(dayList[i], dayList[i+1])
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
