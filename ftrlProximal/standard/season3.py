import sys, os
import datetime
import multiprocessing
import time
sys.path.append('../../lib/fileDB/')
from fileDB import FileDB
sys.path.append('../../lib/featureSelector/')
from poissonInclusion import PoissonInclusion
sys.path.append('../../lib/classifier/')
from ftrlProximal import FTRLProximal
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
def train(trainingDB, poissonInclusion, classifier):
	lastShowTime=datetime.datetime.min
	while True:
		try:
			x, y, currentTime=trainingDB.next()
			selectedX=poissonInclusion.transform(x)
			Y=int(y)
			classifier.update(selectedX, Y)
			if currentTime-lastShowTime>datetime.timedelta(minutes=60):
				print currentTime, "run at ", datetime.datetime.now()
				lastShowTime=currentTime
		except StopIteration as stopIteration:
			break
def onlineRun(testingDB, poissonInclusion, classifier, outFilename):
	file=open(outFilename, "w")
	while True:
		try:
			x, y, currentTime=testingDB.next()
			selectedX=poissonInclusion.transform(x)
			Y=int(y)
			p=classifier.predict(selectedX)
			file.write(str(currentTime)+", "+str(Y==1)+", "+str(p)+"\n")
			classifier.update(selectedX, Y)
		except StopIteration as stopIteration:
			break
	file.close()
def closeDB(trainingDB, testingDB):
	trainingDB.close()
	testingDB.close()
def run(p, trainingDay, testingDay):
	trainingDB, testingDB=prepareDB([trainingDay+".log"], [testingDay+".log"])
	poissonInclusion=PoissonInclusion(p)
	classifier=FTRLProximal(alpha=0.1, beta=1, lambda1=0.1, lambda2=0.1)
	#train(trainingDB, poissonInclusion, classifier)
	onlineRun(testingDB, poissonInclusion, classifier, "./log/season3/"+testingDay+"/"+str(p)+".log")
	closeDB(trainingDB, testingDB)
def main():
	dayList=["2013-10-19", "2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
	for p in [0.001, 0.03]:
		processList=list()
		for i in range(len(dayList)-1):
			dirname="./log/season3/"+dayList[i+1]+"/"
			if not os.path.isdir(dirname):
				os.mkdir(dirname)
			process=multiprocessing.Process(target=run, args=(p, dayList[i], dayList[i+1]))
			process.start()
			processList.append(process)
			time.sleep(60)
		for process in processList:
			process.join()	
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
