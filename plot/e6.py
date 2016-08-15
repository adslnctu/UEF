import numpy as np
import sys, os
def getTime(filename, dataSize):
    with open(filename) as file:
        s=file.next().replace("\n", "")
        ss=[float(a) for a in s.split(":")]
        datetime.timedelta(hours=ss[0], minutes=ss[1], seconds=ss[2])
        bb=datetime.timedelta(hours=ss[0], minutes=ss[1], seconds=ss[2])
        return 1000.0*bb.seconds/dataSize
dayList=["2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
lrTimeList=list()
lrfhTimeList=list()
ftrlTimeList=list()
semTimeList=list()
ssemTimeList=list()
for day in dayList:
    with open("/home/chaowang/ftrlProximal/standard/log/season2/"+day+"/0.03.log") as file:
        dataSize=len(file.readlines())
    lrTimeList.append(getTime("/home/chaowang/lr/onlineTime/log/season2/"+day+".log", dataSize))
    lrfhTimeList.append(getTime("/home/chaowang/lr_fh/onlineTime/log/season2/"+day+".log", dataSize))
    ftrlTimeList.append(getTime("/home/chaowang/ftrlProximal/runTime/log/season2/"+day+".log", dataSize))
    semTimeList.append(getTime("/home/chaowang/sem/onlineTime/log/season2/"+day+"/30.log", 50000))
    ssemTimeList.append(getTime("/home/chaowang/ssem/onlineTime/log/season2/"+day+"/30.log", 50000))
with open("./data/e6_a.dat", "w") as file:
    for i, lrTime, lrfhTime, ftrlTime, semTime, ssemTime in zip(range(len(dayList)), lrTimeList, lrfhTimeList, ftrlTimeList, semTimeList, ssemTimeList):
        file.write("%d %f %f %f %f %f\n"%(i, lrTime, lrfhTime, ftrlTime, semTime, ssemTime))
