from onlineClassifier import OnlineClassifier
class SingleDimCounter():
	def __init__(self):
		initailValue=0.001
		self.valueCountDict={"click": {-3.0: initailValue, -2.0: initailValue, -1.0: initailValue, 0.0: initailValue, 1.0: initailValue, 2.0: initailValue, 3.0: initailValue}, "noclick": {-3.0: initailValue, -2.0: initailValue, -1.0: initailValue, 0.0: initailValue, 1.0: initailValue, 2.0: initailValue, 3.0: initailValue}}
	def update(self, xi, Y):
		if Y==1:
			if not self.valueCountDict["click"].has_key(xi):
				self.valueCountDict["click"][xi]=0
			self.valueCountDict["click"][xi]+=1
		else:
			if not self.valueCountDict["noclick"].has_key(xi):
				self.valueCountDict["noclick"][xi]=0
			self.valueCountDict["noclick"][xi]+=1
	def getProbOfXGivenY(self, xi, Y):#p(xi|click=True) or p(xi|click=False)
		if Y==1:
			targetDict=self.valueCountDict["click"]
		else:
			targetDict=self.valueCountDict["noclick"]
		if targetDict.has_key(xi):
			return 1.0*targetDict[xi]/sum(targetDict.values())
		else:
			return 0.0
class NaiveBayesClassifier(OnlineClassifier):
	def __init__(self, targetDimList):
		self.clickCount=0.1
		self.noclickCount=0.1
		self.targetDimList=targetDimList
		self.singleDimCounterList=[SingleDimCounter()]*len(targetDimList)
	def update(self, X, Y):
		newX=[X[i] for i in self.targetDimList]
		if Y==1:
			self.clickCount+=1
		else:
			self.noclickCount+=1
		for xi, singleDimCounter in zip(newX, self.singleDimCounterList):
			singleDimCounter.update(xi, Y)
	def predict(self, X):
		newX=[X[i] for i in self.targetDimList]
		clickProduct=1.0
		noClickProduct=1.0
		for xi, singleDimCounter in zip(newX, self.singleDimCounterList):	
			clickProduct*=singleDimCounter.getProbOfXGivenY(xi, 1)
			noClickProduct*=singleDimCounter.getProbOfXGivenY(xi, 0)
		probOfXAndClick=clickProduct*self.clickCount/(self.clickCount+self.noclickCount)
		probOfXAndNoclick=noClickProduct*self.noclickCount/(self.clickCount+self.noclickCount)
		return probOfXAndClick/(probOfXAndClick+probOfXAndNoclick)
