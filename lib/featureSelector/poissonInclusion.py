import numpy as np
from scipy.sparse import coo_matrix
import random
import pickle
from orderedset import OrderedSet
def anyToString(a):
	if type(a)==unicode:
		return a
	else:
		return str(a)
def nestedxTox(x):
	newx=dict()
	for key in x.keys():
		k=anyToString(key)
		value=x[key]
		if type(value)==dict:
			childx=nestedxTox(value)
			for childKey in childx.keys():
				newx[k+"_"+anyToString(childKey)]=childx[childKey]
		else:
			newx[k+"_"+anyToString(value)]=1
	return newx
class PoissonInclusion2():
	def __init__(self, p):
		self.p=p
		self.featureSize=0
		self.featureDict=dict()
	def transform(self, x):
		newx=nestedxTox(x)
		colList=list()
		dataList=list()
		for key in newx:
			if not key in self.featureDict:
				if random.random()<self.p:
					self.featureDict[key]=self.featureSize
					self.featureSize+=1
					colList.append(self.featureSize-1)
					dataList.append(newx[key])
			else:
				colList.append(self.featureDict[key])
				dataList.append(newx[key])
		row=np.array([0]*len(colList))
		col=np.array(colList)
		data=np.array(dataList)
		if len(col)==0:
			return None
		else:
			return coo_matrix((data,(row, col)))
