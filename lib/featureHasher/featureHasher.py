from sklearn.feature_extraction import FeatureHasher as FH
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
class FeatureHasher():
	def __init__(self, n_features):
		self.hasher=FH(n_features=n_features, input_type="dict")        
	def transform(self, x):
		newx=nestedxTox(x)
		X=self.hasher.transform([newx]).todok()
		return X
	def transformList(self, xList):
		newxList=[nestedxTox(x) for x in xList]
		X=self.hasher.transform(newxList).todok()
		return X
