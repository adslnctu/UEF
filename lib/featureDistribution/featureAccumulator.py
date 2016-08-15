import itertools
class FeatureAccumulator():
	def __init__(self, n_features):
		self.numOfX=0
		self.n_features=n_features
		self.featureCountList=list()
		for i in range(0, n_features):
			self.featureCountList.append(dict())
	def addX(self, X):
		self.numOfX+=1
		cX=X.tocoo()
		for i, xi in itertools.izip(cX.col, cX.data):
			if not self.featureCountList[i].has_key(xi):
				self.featureCountList[i][xi]=0
			self.featureCountList[i][xi]+=1
