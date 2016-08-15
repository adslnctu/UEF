import sys, os
import datetime
import numpy
import math
import pickle
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
sys.path.append('../../lib/fileDB/')
from fileDB import FileDB
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
def train(trainingDB, classifier, dictVectorizer):
	lastShowTime=datetime.datetime.min
	xList=list()
	yList=list()
	trainingSize=0
	while True:
		try:
			x, y, currentTime=trainingDB.next()
			xList.append(x)
			yList.append(y)
			trainingSize+=1
			if currentTime-lastShowTime>datetime.timedelta(hours=1):
				print currentTime, "run at ", datetime.datetime.now()
				lastShowTime=currentTime
		except StopIteration as stopIteration:
			break
	dictVectorizer.fit(xList)
	X=dictVectorizer.transform(xList)
	Y=numpy.array(yList)
	classifier.fit(X, Y)
def onlineRun(testingDB, classifier, dictVectorizer):
	lastShowTime=datetime.datetime.min
	while True:
		try:
			x, y, currentTime=testingDB.next()
			X=dictVectorizer.transform([x])
			Y=numpy.array([y])
			P=classifier.predict_proba(X)[:, 1]
			if currentTime-lastShowTime>datetime.timedelta(hours=1):
				print currentTime, "run at ", datetime.datetime.now()
				lastShowTime=currentTime
		except StopIteration as stopIteration:
			break
def closeDB(trainingDB, testingDB):
	trainingDB.close()
	testingDB.close()
def run(trainingDay, testingDay):
	trainingDB, testingDB=prepareDB([trainingDay+".log"], [testingDay+".log"])
	classifier=prepareClassifier()
	dictVectorizer=DictVectorizer(sparse=True)
	start=datetime.datetime.now()
	train(trainingDB, classifier, dictVectorizer)
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
