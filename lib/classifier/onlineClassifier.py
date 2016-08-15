class OnlineClassifier():
	def __init__(self):
		pass
	def update(self, X, Y):
		raise NotImplementedError( "virtualMethod is virutal! Must be overwrited." )
	def predict(self, X):
		raise NotImplementedError( "virtualMethod is virutal! Must be overwrited." )
