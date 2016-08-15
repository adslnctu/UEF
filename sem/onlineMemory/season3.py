import sys, os
import datetime
import numpy
import math
import resource
import time
import pickle
import random
import numpy as np
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
	sem=SEM(beta0=beta0, decay=decay, XSize=XSize, classifierList=classifierList)
	a=list()
	for i in range(XSize):
		a.append(list())
		for j in range(XSize):
			a[i].append(random.uniform(-5.0, 5.0))
	sem.eta=np.matrix(a)
	return sem
def onlineRun(testingDB, featureHasher, featureSelector, classifier):
	i=0
	while True:
		try:
			x, y, currentTime=testingDB.next()
			X=featureHasher.transform(x)
			Y=int(y)
			selectedX=featureSelector.transform(X)
			p=classifier.predict(selectedX)
			#classifier.update(selectedX, Y)
			if i>50000:
				break
			i+=1
		except StopIteration as stopIteration:
			break
def closeDB(trainingDB, testingDB):
	trainingDB.close()
	testingDB.close()
def run(beta0, selectSize, trainingDay, testingDay):
	decay=0.0
	trainingDB, testingDB=prepareDB([trainingDay+".log"], [testingDay+".log"])
	featureHasher=FeatureHasher(pow(2, 20))
	targetDimList=pickle.load(open("./targetDimList/season3/"+trainingDay+".pickle", "rb"))
	featureSelector=SignificantFeatureSelector(targetDimList=targetDimList[:selectSize])
	classifier=prepareClassifier(beta0=beta0, decay=decay, XSize=selectSize)
	#train(trainingDB, featureHasher, featureSelector, classifier)
	onlineRun(testingDB, featureHasher, featureSelector, classifier)
	file=open("./log/season3/"+testingDay+"/"+str(selectSize)+".log", "w", 0)
	memory=float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)/1024
	file.write(str(memory)+"\n")
	file.close()
	closeDB(trainingDB, testingDB)
def main():
	dayList=[sys.argv[1], sys.argv[2]]
	selectSize=int(sys.argv[3])
	beta0=1.0
	dirname="./log/season3/"+dayList[1]+"/"
	if not os.path.isdir(dirname):
		os.mkdir(dirname)
	run(beta0, selectSize, dayList[0], dayList[1])
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
