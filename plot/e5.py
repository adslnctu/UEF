import numpy as np
import sys, os
from sklearn.metrics import roc_curve, auc, log_loss
def getMem(filename):
	with open(filename, "r") as file:
		for line in file:
			mem=float(line.replace("\n", ""))
	return mem
semAvgMemoryList=list()
ssemAvgMemoryList=list()
dayList=["2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
kList=[1, 20, 30, 40, 60, 80, 100, 200, 300, 400, 500]
for k in kList:
	semMemList=list()
	ssemMemList=list()
	for day in dayList:
		semMem=getMem("/home/chaowang/sem/offlineMemory/log/season2/"+day+"/"+str(k)+".log")
		ssemMem=getMem("/home/chaowang/ssem/offlineMemory/log/season2/"+day+"/"+str(k)+".log")
		semMemList.append(semMem)
		ssemMemList.append(ssemMem)
	semAvgMemoryList.append(np.mean(semMemList))
	ssemAvgMemoryList.append(np.mean(ssemMemList))
with open("./data/e5_a.dat", "w") as file:
	for k, semAvgMemory, ssemAvgMemory in zip(kList, semAvgMemoryList, ssemAvgMemoryList):
		file.write("%d %f %f\n"%(k, semAvgMemory, ssemAvgMemory))

semAvgMemoryList=list()
ssemAvgMemoryList=list()
dayList=["2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
kList=[1, 20, 30, 40, 60, 80, 100, 200, 300, 400, 500]
for k in kList:
	semMemList=list()
	ssemMemList=list()
	for day in dayList:
		semMem=getMem("/home/chaowang/sem/offlineMemory/log/season3/"+day+"/"+str(k)+".log")
		ssemMem=getMem("/home/chaowang/ssem/offlineMemory/log/season3/"+day+"/"+str(k)+".log")
		semMemList.append(semMem)
		ssemMemList.append(ssemMem)
	semAvgMemoryList.append(np.mean(semMemList))
	ssemAvgMemoryList.append(np.mean(ssemMemList))
with open("./data/e5_b.dat", "w") as file:
	for k, semAvgMemory, ssemAvgMemory in zip(kList, semAvgMemoryList, ssemAvgMemoryList):
		file.write("%d %f %f\n"%(k, semAvgMemory, ssemAvgMemory))
