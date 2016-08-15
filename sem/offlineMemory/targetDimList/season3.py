import sys, os
import pickle
sys.path.append('../../../lib/featureSelector/')
from significantFeatureSelector import SignificantFeatureSelector
def main():
	dayList=["2013-10-19", "2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
	for i in range(len(dayList)-1):
		for selectSize in [500]:
			featureSelector=SignificantFeatureSelector("../../../lib/featureDistribution/pickle/season3/"+dayList[i]+".pickle", selectSize=selectSize)
			filename="./season3/"+dayList[i]+".pickle"
			pickle.dump(featureSelector.targetDimList, open(filename, "w"))
if __name__=="__main__":
        sys.stdout=os.fdopen(sys.stdout.fileno(), 'w', 0)
	main()
