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
		trainingDBFilenameList.append("../../lib/fileDB/log/season2/"+filename)
	trainingDB=FileDB(trainingDBFilenameList)

	testingDBFilenameList=list()
	for filename in testingFilenameList:
		testingDBFilenameList.append("../../lib/fileDB/log/season2/"+filename)
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
def onlineRun(testingDB, classifier, featureHasher):
	while True:
		try:
			x, y, currentTime=testingDB.next()
			a=featureHasher.transform(x)
			p=classifier.predict_proba(a)[:, 1][0]
		except StopIteration as stopIteration:
			break
def closeDB(trainingDB, testingDB):
	trainingDB.close()
	testingDB.close()
def run(trainingDay, testingDay):
	trainingDB, testingDB=prepareDB([trainingDay+".log"], [testingDay+".log"])
	classifier=prepareClassifier()
	featureHasher=FeatureHasher(pow(2, 18))
	train(trainingDB, classifier, featureHasher)
	start=datetime.datetime.now()
	onlineRun(testingDB, classifier, featureHasher)
	end=datetime.datetime.now()
	file=open("./log/season2/"+testingDay+".log", "w")
	file.write(str(end-start)+"\n")
	file.close()
	closeDB(trainingDB, testingDB)
def main():
	dayList=["2013-06-06", "2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
	for i in range(len(dayList)-1):
		run(dayList[i], dayList[i+1])
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
