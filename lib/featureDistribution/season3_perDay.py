import sys, os
import itertools
import datetime
import pickle
from featureAccumulator import FeatureAccumulator
sys.path.append('../featureHasher/')
from featureHasher import FeatureHasher
sys.path.append('../fileDB/')
from fileDB import FileDB
def run(data, date):
	trainingDBFilenameList=list()
	trainingDBFilenameList.append("../lib/fileDB/log/"+data+"/"+date+".log")
	featureSize=pow(2, 20)
	featureHasher=FeatureHasher(featureSize)
	trainingDB=FileDB(trainingDBFilenameList)
	clickFeatureAccumulator=FeatureAccumulator(n_features=featureSize)
	noclickFeatureAccumulator=FeatureAccumulator(n_features=featureSize)
	lastOutputTime=datetime.datetime.min
	while True:
		try:
			x, y, currentTime=trainingDB.next()
			X, Y=featureHasher.transform(x, y)
			if Y==1:
				clickFeatureAccumulator.addX(X)
			else:
				noclickFeatureAccumulator.addX(X)
			if currentTime-lastOutputTime>datetime.timedelta(minutes=60):
				print currentTime
				print "numOfClick", clickFeatureAccumulator.numOfX
				print "numOfNoClick", noclickFeatureAccumulator.numOfX
				lastOutputTime=currentTime
		except StopIteration as stopIteration:
			break
	trainingDB.close()
	pickle.dump((clickFeatureAccumulator, noclickFeatureAccumulator), open("./pickle/"+data+"/"+date+".pickle", "w"))
def main():
	dateList=["2013-10-19", "2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
	for date in dateList:
		data="season3"
		print "./pickle/"+data+"/"+date+".pickle"
		run(data, date)
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
