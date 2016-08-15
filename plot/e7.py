import datetime
import numpy as np
def getTime(filename):
	with open(filename, "r") as file:
		for line in file:
			ss=line.replace("\n", "").split(":")
			time=datetime.timedelta(hours=float(ss[0]), minutes=float(ss[1]), seconds=float(ss[2]))
	return time.seconds+1.0*time.microseconds/1000000
semAvgTimeList=list()
ssemAvgTimeList=list()
dayList=["2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
kList=[1, 20, 30, 40, 60, 80, 100, 200, 300, 400, 500]
for k in kList:
	semTimeList=list()
	ssemTimeList=list()
	for day in dayList:
	   	semTime=getTime("/home/chaowang/sem/offlineTime/log/season2/"+day+"/"+str(k)+".log")
		ssemTime=getTime("/home/chaowang/ssem/offlineTime/log/season2/"+day+"/"+str(k)+".log")
		semTimeList.append(semTime)
		ssemTimeList.append(ssemTime)
	semAvgTimeList.append(np.mean(semTimeList))
	ssemAvgTimeList.append(np.mean(ssemTimeList))
with open("./data/e7_a.dat", "w") as file:
	for k, semAvgTime, ssemAvgTime in zip(kList, semAvgTimeList, ssemAvgTimeList):
		file.write("%d %f %f\n"%(k, semAvgTime, ssemAvgTime))
semAvgTimeList=list()
ssemAvgTimeList=list()
dayList=["2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
kList=[1, 20, 30, 40, 60, 80, 100, 200, 300, 400, 500]
for k in kList:
	semTimeList=list()
	ssemTimeList=list()
	for day in dayList:
	   	semTime=getTime("/home/chaowang/sem/offlineTime/log/season3/"+day+"/"+str(k)+".log")
		ssemTime=getTime("/home/chaowang/ssem/offlineTime/log/season3/"+day+"/"+str(k)+".log")
		semTimeList.append(semTime)
		ssemTimeList.append(ssemTime)
	semAvgTimeList.append(np.mean(semTimeList))
	ssemAvgTimeList.append(np.mean(ssemTimeList))
with open("./data/e7_b.dat", "w") as file:
	for k, semAvgTime, ssemAvgTime in zip(kList, semAvgTimeList, ssemAvgTimeList):
		file.write("%d %f %f\n"%(k, semAvgTime, ssemAvgTime))
