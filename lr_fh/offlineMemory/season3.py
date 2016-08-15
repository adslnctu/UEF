import sys, os
import datetime
import numpy
import math
import pickle
import resource
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
def train(trainingDB, classifier, featureHasher, outFilename):
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
	file=open(outFilename, "w")
	memory=float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)/1024
	file.write(str(memory)+"\n")
	file.close()
def closeDB(trainingDB, testingDB):
	trainingDB.close()
	testingDB.close()
def run(trainingDay, testingDay):
	trainingDB, testingDB=prepareDB([trainingDay+".log"], [testingDay+".log"])
	classifier=prepareClassifier()
	featureHasher=FeatureHasher(pow(2, 18))
	outFilename="./log/season3/"+testingDay+".log"
	train(trainingDB, classifier, featureHasher, outFilename)
	closeDB(trainingDB, testingDB)
def main():
	dayList=[sys.argv[1], sys.argv[2]]
	for i in range(len(dayList)-1):
		run(dayList[i], dayList[i+1])
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
