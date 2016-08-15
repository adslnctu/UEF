import math
import numpy as np
import scipy.sparse as sparse
import itertools
from onlineClassifier import OnlineClassifier
def sigmoid(a):
	return 1.0/(1+math.pow(math.e, -a))
class FTRLProximal(OnlineClassifier):
	def __init__(self, alpha, beta, lambda1, lambda2):
		self.alpha=alpha
		self.beta=beta
		self.lambda1=lambda1
		self.lambda2=lambda2
		self.zList=list()
		self.nList=list()
		#self.d=n_features
		#self.zList=[0.0]*self.d
		#self.nList=[0.0]*self.d
	def getw(self, i):
		zi=self.zList[i]
		ni=self.nList[i]
		if abs(zi)<=self.lambda1:
			wi=0
		else:
			sign=int(zi>0)
			wi=-1/((self.beta+math.sqrt(ni))/self.alpha+self.lambda2)*(zi-sign*self.lambda1)
		return wi
	def predict(self, X):
		if X is None:
			return 0.5
		else:
			maxIndex=max(X.col)
			newDimSize=(maxIndex+1)-len(self.zList)
			if newDimSize>0:
				self.zList.extend([0.0]*newDimSize)
				self.nList.extend([0.0]*newDimSize)
			if len(self.zList)==0:
				return 0.5
			if isinstance(X, np.ndarray):
				cX=sparse.csr_matrix(X).tocoo()
			else:
				cX=X.tocoo()
			a=0
			for i, xi in itertools.izip(cX.col, cX.data):
				wi=self.getw(i)
				a+=wi*xi
			p=sigmoid(a)
			return p
	def update(self, X, Y):
		if X is None:
			return
		else:
			p=self.predict(X)
			if isinstance(X, np.ndarray):
				cX=sparse.csr_matrix(X).tocoo()
			else:
				cX=X.tocoo()
			for i, xi in itertools.izip(cX.col, cX.data):
				zi=self.zList[i]
				ni=self.nList[i]
				wi=self.getw(i)
				gi=(p-Y)*xi
				sigmai=1.0/self.alpha*(math.sqrt(ni+math.pow(gi, 2))-math.sqrt(ni))
				zi=zi+gi-sigmai*wi
				ni=ni+math.pow(gi, 2)
				self.zList[i]=zi
				self.nList[i]=ni
