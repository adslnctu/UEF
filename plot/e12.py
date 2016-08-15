import numpy as np
import sys, os
def getMem(filename):
    with open(filename, "r") as file:
        for line in file:
            mem=float(line.replace("\n", ""))
    return mem
lrMemoryList=list()
lrfhMemoryList=list()
semMemoryList=list()
ssemMemoryList=list()
dayList=["2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
for day in dayList:
    lrMem=getMem("/home/chaowang/lr/offlineMemory/log/season2/"+day+".log")
    lrfhMem=getMem("/home/chaowang/lr_fh/offlineMemory/log/season2/"+day+".log")
    semMem=getMem("/home/chaowang/sem/offlineMemory/log/season2/"+day+"/30.log")
    ssemMem=getMem("/home/chaowang/ssem/offlineMemory/log/season2/"+day+"/30.log")
    lrMemoryList.append(lrMem)
    lrfhMemoryList.append(lrfhMem)
    semMemoryList.append(semMem)
    ssemMemoryList.append(ssemMem)
with open("./data/e12_a.dat", "w") as file:
	for i, lrMem, lrfhMem, semMem, ssemMem in zip(range(len(dayList)), lrMemoryList, lrfhMemoryList, semMemoryList, ssemMemoryList):
		file.write("%d %f %f %f %f\n"%(i, lrMem, lrfhMem, semMem, ssemMem))
lrMemoryList=list()
lrfhMemoryList=list()
semMemoryList=list()
ssemMemoryList=list()
dayList=["2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
for day in dayList:
    lrMem=getMem("/home/chaowang/lr/offlineMemory/log/season3/"+day+".log")
    lrfhMem=getMem("/home/chaowang/lr_fh/offlineMemory/log/season3/"+day+".log")
    semMem=getMem("/home/chaowang/sem/offlineMemory/log/season3/"+day+"/40.log")
    ssemMem=getMem("/home/chaowang/ssem/offlineMemory/log/season3/"+day+"/40.log")
    lrMemoryList.append(lrMem)
    lrfhMemoryList.append(lrfhMem)
    semMemoryList.append(semMem)
    ssemMemoryList.append(ssemMem)
with open("./data/e12_b.dat", "w") as file:
	for i, lrMem, lrfhMem, semMem, ssemMem in zip(range(len(dayList)), lrMemoryList, lrfhMemoryList, semMemoryList, ssemMemoryList):
		file.write("%d %f %f %f %f\n"%(i, lrMem, lrfhMem, semMem, ssemMem))
