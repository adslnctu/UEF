import numpy as np
import sys, os
def getMem(filename):
    with open(filename, "r") as file:
        for line in file:
            mem=float(line.replace("\n", ""))
    return mem
semAvgMemoryList=list()
ssemAvgMemoryList=list()
dayList=["2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
kList=[1, 30, 50, 100, 200, 300, 400, 500]
for k in kList:
    semMemoryList=list()
    ssemMemoryList=list()
    for day in dayList:
        semMem=getMem("/home/chaowang/sem/onlineMemory/log/season2/"+day+"/"+str(k)+".log")
        ssemMem=getMem("/home/chaowang/ssem/onlineMemory/log/season2/"+day+"/"+str(k)+".log")
        semMemoryList.append(semMem)
        ssemMemoryList.append(ssemMem)
    semAvgMemoryList.append(np.mean(semMemoryList))
    ssemAvgMemoryList.append(np.mean(ssemMemoryList))
with open("./data/e11_a.dat", "w") as file:
    for k, semAvgMemory, ssemAvgMemory in zip(kList, semAvgMemoryList, ssemAvgMemoryList):
        file.write("%d %f %f\n"%(k, semAvgMemory, ssemAvgMemory))
semAvgMemoryList=list()
ssemAvgMemoryList=list()
dayList=["2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
kList=[1, 40, 50, 100, 200, 300, 400, 500]
for k in kList:
    semMemoryList=list()
    ssemMemoryList=list()
    for day in dayList:
        semMem=getMem("/home/chaowang/sem/onlineMemory/log/season3/"+day+"/"+str(k)+".log")
        ssemMem=getMem("/home/chaowang/ssem/onlineMemory/log/season3/"+day+"/"+str(k)+".log")
        semMemoryList.append(semMem)
        ssemMemoryList.append(ssemMem)
    semAvgMemoryList.append(np.mean(semMemoryList))
    ssemAvgMemoryList.append(np.mean(ssemMemoryList))
with open("./data/e11_b.dat", "w") as file:
    for k, semAvgMemory, ssemAvgMemory in zip(kList, semAvgMemoryList, ssemAvgMemoryList):
        file.write("%d %f %f\n"%(k, semAvgMemory, ssemAvgMemory))
