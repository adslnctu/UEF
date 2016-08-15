import pickle
import heapq
import itertools
import sys, os
sys.path.append('/home/chaowang/lib/featureDistribution/')
from featureAccumulator import FeatureAccumulator
def getMeanOf(featureAccumulator, i):
	sum=0
	for value in featureAccumulator.featureCountList[i].keys():
		sum+=value*featureAccumulator.featureCountList[i][value]
	return sum/featureAccumulator.numOfX
def getAbsMeanDiffOf(featureAccumulator1, featureAccumulator2, i):
	return abs(getMeanOf(featureAccumulator1, i)-getMeanOf(featureAccumulator2, i))
def getKDistinList(k, data, date):
	clickFeatureAccumulator, noclickFeatureAccumulator=pickle.load(open("/home/chaowang/lib/featureDistribution/pickle/"+data+"/"+date+".pickle", "rb"))
	AbsMeanDiffList=list()
	for i in range(clickFeatureAccumulator.n_features):
		AbsMeanDiff=getAbsMeanDiffOf(clickFeatureAccumulator, noclickFeatureAccumulator, i)
		AbsMeanDiffList.append(AbsMeanDiff)
	topList=heapq.nlargest(k, zip(AbsMeanDiffList, itertools.count()))
	i=list()
	for AbsMeanDiff, index in topList:
		i.append(AbsMeanDiff)
	return i
dayList=["2013-06-06", "2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
i=0
for day in dayList:
	kDistinList=getKDistinList(100, "season2", day)
	with open("./data/e10_"+chr(ord('a')+i)+".dat", "w") as file:
		for k, kDistin in zip(range(len(kDistinList)), kDistinList):
			file.write("%d %f\n"%(k, kDistin))
		i+=1
dayList=["2013-10-19", "2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
for day in dayList:
	kDistinList=getKDistinList(100, "season3", day)
	with open("./data/e10_"+chr(ord('a')+i)+".dat", "w") as file:
		for k, kDistin in zip(range(len(kDistinList)), kDistinList):
			file.write("%d %f\n"%(k, kDistin))
		i+=1
