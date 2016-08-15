import sys
import pickle
import heapq
import itertools
import numpy as np
sys.path.append('/home/chaowang/lib/featureDistribution/')
from featureAccumulator import FeatureAccumulator
def getMean(featureAccumulator, i):
	sum=0
	for value in featureAccumulator.featureCountList[i].keys():
		sum+=value*featureAccumulator.featureCountList[i][value]
	return sum/featureAccumulator.numOfX
class SignificantFeatureSelector():
	def __init__(self, filename=None, selectSize=None, targetDimList=None):
		if targetDimList==None:
			clickFeatureAccumulator, noclickFeatureAccumulator=pickle.load(open(filename, "rb"))
			absMeanDiffList=list()
			for i in range(clickFeatureAccumulator.n_features):
				absMeanDiff=abs(getMean(clickFeatureAccumulator, i)-getMean(noclickFeatureAccumulator, i))
				absMeanDiffList.append(absMeanDiff)
			self.targetDimList=list()
			topList=heapq.nlargest(selectSize, zip(absMeanDiffList, itertools.count()))
			for absMeanDiff, index in topList:
				self.targetDimList.append(index)
		else:
			self.targetDimList=targetDimList
	def transform(self, X):
		Xnew=list()
		for dim in self.targetDimList:
			Xnew.append(float(X[0, dim]))
		return np.array(Xnew)
