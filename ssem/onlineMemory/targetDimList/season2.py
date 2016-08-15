import sys, os
import pickle
sys.path.append('../../../lib/featureSelector/')
from significantFeatureSelector import SignificantFeatureSelector
def main():
	dayList=["2013-06-06", "2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
	for i in range(len(dayList)-1):
		for selectSize in [500]:
			featureSelector=SignificantFeatureSelector("../../../lib/featureDistribution/pickle/season2/"+dayList[i]+".pickle", selectSize=selectSize)
			filename="./season2/"+dayList[i]+".pickle"
			pickle.dump(featureSelector.targetDimList, open(filename, "w"))
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
