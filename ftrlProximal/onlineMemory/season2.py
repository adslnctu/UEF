import sys, os
import datetime
from pympler import asizeof
import multiprocessing
import time
import pickle
import resource
sys.path.append('../../lib/fileDB/')
from fileDB import FileDB
sys.path.append('../../lib/featureSelector/')
from poissonInclusion import PoissonInclusion
sys.path.append('../../lib/classifier/')
from ftrlProximal import FTRLProximal
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
def train(trainingDB, poissonInclusion, classifier):
	while True:
		try:
			x, y, currentTime=trainingDB.next()
			selectedX=poissonInclusion.transform(x)
			Y=int(y)
			classifier.update(selectedX, Y)
		except StopIteration as stopIteration:
			break
def onlineRun(testingDB, poissonInclusion, classifier):
	while True:
		try:
			x, y, currentTime=testingDB.next()
			selectedX=poissonInclusion.transform(x)
			Y=int(y)
			p=classifier.predict(selectedX)
			classifier.update(selectedX, Y)
		except StopIteration as stopIteration:
			break
def closeDB(trainingDB, testingDB):
	trainingDB.close()
	testingDB.close()
def run(p, trainingDay, testingDay):
	trainingDB, testingDB=prepareDB([trainingDay+".log"], [testingDay+".log"])
	poissonInclusion=PoissonInclusion(p)
	classifier=FTRLProximal(alpha=0.1, beta=1, lambda1=0.1, lambda2=0.1)
	#train(trainingDB, poissonInclusion, classifier)
	onlineRun(testingDB, poissonInclusion, classifier)
	file=open("./log/season2/"+testingDay+".log", "w", 0)
	memory=float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)/1024
	file.write(str(memory))
	file.close()
	closeDB(trainingDB, testingDB)
def main():
	dayList=["2013-06-06", "2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
	for p in [0.03]:
		processList=list()
		for i in range(len(dayList)-1):
			process=multiprocessing.Process(target=run, args=(p, dayList[i], dayList[i+1]))
			process.start()
			processList.append(process)
		for process in processList:
			process.join()	
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
