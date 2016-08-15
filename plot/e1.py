import pickle
import sys
import heapq
import itertools
import numpy as np
sys.path.append('/home/chaowang/lib/featureDistribution/')
from featureAccumulator import FeatureAccumulator
def getMeanOf(featureAccumulator, i):
	sum=0
	for value in featureAccumulator.featureCountList[i].keys():
		sum+=value*featureAccumulator.featureCountList[i][value]
	return sum/featureAccumulator.numOfX
def getAbsMeanDiffOf(featureAccumulator1, featureAccumulator2, i):
	return abs(getMeanOf(featureAccumulator1, i)-getMeanOf(featureAccumulator2, i))
def getTopkList(clickFeatureAccumulator, noclickFeatureAccumulator, k):
	AbsMeanDiffList=list()
	for i in range(clickFeatureAccumulator.n_features):
		AbsMeanDiff=getAbsMeanDiffOf(clickFeatureAccumulator, noclickFeatureAccumulator, i)
		AbsMeanDiffList.append(AbsMeanDiff)
	topkList=heapq.nlargest(k, zip(AbsMeanDiffList, itertools.count()))
	return [i[1] for i in topkList]
def getJaccardSimilarity(a, b):
	return 1.0*len(a.intersection(b))/len(a.union(b))
dataDayListDict={"season2": ["2013-06-06", "2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"], "season3": ["2013-10-19", "2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"], "sp_season3": ["2013-10-21", "2013-10-22"]}
dataDayMaxTopkListDict={"season2": dict(), "season3": dict(), "sp_season3": dict()}
for data in dataDayListDict.keys():
	for day in dataDayListDict[data]:
		if data=="sp_season3":
			clickFeatureAccumulator, noclickFeatureAccumulator=pickle.load(open("/home/chaowang/lib/featureDistribution/pickle/season3/"+day+".pickle", "rb"))
		else:
			clickFeatureAccumulator, noclickFeatureAccumulator=pickle.load(open("/home/chaowang/lib/featureDistribution/pickle/"+data+"/"+day+".pickle", "rb"))
		maxTopkList=getTopkList(clickFeatureAccumulator, noclickFeatureAccumulator, 100)
		dataDayMaxTopkListDict[data][day]=maxTopkList
dataList=["season2", "season3", "sp_season3"]
kList=[1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 70, 80, 90, 100]
dd=list()
for data in dataList:
	jaccardSimilarityMeanList=list()
	for k in kList:
		jaccardSimilarityList=list()
		dayList=dataDayMaxTopkListDict[data].keys()
		for i in range(len(dayList)):
			for j in range(i+1, len(dayList)):
				day1MaxTopkSet=set(dataDayMaxTopkListDict[data][dayList[i]][:k])
				day2MaxTopkSet=set(dataDayMaxTopkListDict[data][dayList[j]][:k])
				jaccardSimilarityList.append(getJaccardSimilarity(day1MaxTopkSet, day2MaxTopkSet))
		jaccardSimilarityMeanList.append(np.mean(jaccardSimilarityList))
	dd.append(jaccardSimilarityMeanList)
with open("./data/e1.dat", "w") as file:
	for k, a, b, c in zip(kList, dd[0], dd[1], dd[2]):
		file.write("%d %f %f %f\n"%(k, a, b, c))
