import datetime
import numpy as np
import sys, os
def getTime(filename, dataSize):
    with open(filename, "r") as file:
        for line in file:
            ss=line.replace("\n", "").split(":")
            time=datetime.timedelta(hours=float(ss[0]), minutes=float(ss[1]), seconds=float(ss[2]))
    return (time.seconds+1.0*time.microseconds/1000000)/dataSize*1000
semMemoryList=list()
ssemMemoryList=list()
dayList=["2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
kList=[1, 30, 50, 100, 200, 300, 400, 500]
for k in kList:
    cc=list()
    dd=list()
    for day in dayList:
        semMem=getTime("/home/chaowang/sem/onlineTime/log/season2/"+day+"/"+str(k)+".log", 50000)
        ssemMem=getTime("/home/chaowang/ssem/onlineTime/log/season2/"+day+"/"+str(k)+".log", 50000)
        cc.append(semMem)
        dd.append(ssemMem)
    semMemoryList.append(np.mean(cc))
    ssemMemoryList.append(np.mean(dd))
with open("./data/e13_a.dat", "w") as file:
    for k, semMemory, ssemMemory in zip(kList, semMemoryList, ssemMemoryList):
        file.write("%d %f %f\n"%(k, semMemory, ssemMemory))
semMemoryList=list()
ssemMemoryList=list()
dayList=["2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
kList=[1, 40, 50, 100, 200, 300, 400, 500]
for k in kList:
    cc=list()
    dd=list()
    for day in dayList:
        semMem=getTime("/home/chaowang/sem/onlineTime/log/season3/"+day+"/"+str(k)+".log", 50000)
        ssemMem=getTime("/home/chaowang/ssem/onlineTime/log/season3/"+day+"/"+str(k)+".log", 50000)
        cc.append(semMem)
        dd.append(ssemMem)
    semMemoryList.append(np.mean(cc))
    ssemMemoryList.append(np.mean(dd))
with open("./data/e13_b.dat", "w") as file:
    for k, semMemory, ssemMemory in zip(kList, semMemoryList, ssemMemoryList):
        file.write("%d %f %f\n"%(k, semMemory, ssemMemory))
