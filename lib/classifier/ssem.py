import math
import numpy as np
from onlineClassifier import OnlineClassifier
def getexpEtaDotXnew(eta, Xnew):
	return pow(math.e, sum([i*j for i, j in zip(eta, Xnew)]))
class SSEM(OnlineClassifier):
	def __init__(self, beta0, decay, XSize, classifierList):
		self.t=0
		self.beta0=beta0
		self.decay=decay
		self.classifierList=classifierList
		self.eta=np.array([0.0]*len(self.classifierList))
	def getg(self):
		t=np.power(math.e, self.eta)
		g=t/t.sum()
		return g
	def updateClassifierList(self, X, Y):
		for classifier in self.classifierList:
			classifier.update(X, Y)
	def updateEta(self, X, Y):
		self.t+=1
		beta=self.beta0/pow(self.t, self.decay)
		fn=self.predict(X)
		g=self.getg()
		fnArray=np.array([classifier.predict(X) for classifier in self.classifierList])
		gradient=np.multiply(g, (fnArray-fn)*(fn-Y)/(fn*(1-fn)))
		self.eta-=beta*gradient
	def update(self, X, Y):
		self.updateEta(X, Y)
		self.updateClassifierList(X, Y)
	def predict(self, X):
		g=self.getg()
		fnArray=np.matrix([classifier.predict(X) for classifier in self.classifierList])
		fn=fnArray.dot(g)[0, 0]
		return fn
