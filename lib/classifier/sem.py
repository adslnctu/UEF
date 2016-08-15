import math
import numpy as np
from onlineClassifier import OnlineClassifier
def getexpEtaDotXnew(eta, Xnew):
	return pow(math.e, sum([i*j for i, j in zip(eta, Xnew)]))
class SEM(OnlineClassifier):
	def __init__(self, beta0, decay, XSize, classifierList):
		self.t=0
		self.beta0=beta0
		self.decay=decay
		self.classifierList=classifierList
		self.eta=np.matrix([[0.0]*XSize]*len(classifierList))
	def getg(self, X):
		Xt=np.reshape(X, (len(X), 1))
		t=np.power(math.e, self.eta.dot(Xt))
		g=t/t.sum(axis=0)
		return g
	def updateClassifierList(self, X, Y):
		for classifier in self.classifierList:
			classifier.update(X, Y)
	def updateEta(self, X, Y):
		self.t+=1
		beta=self.beta0/pow(self.t, self.decay)
		fn=self.predict(X)
		g=self.getg(X)
		fnArray=np.matrix([classifier.predict(X) for classifier in self.classifierList])
		gradient=np.multiply(g, (fnArray-fn).transpose()*(fn-Y)/(fn*(1-fn))).dot(np.matrix(X))
		self.eta-=beta*gradient
	def update(self, X, Y):
		self.updateEta(X, Y)
		self.updateClassifierList(X, Y)
	def predict(self, X):
		g=self.getg(X)
		fnArray=np.matrix([classifier.predict(X) for classifier in self.classifierList])
		fn=fnArray.dot(g)[0, 0]
		return fn
