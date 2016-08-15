import numpy as np
import sys, os
import datetime
def getTime(filename):
    with open(filename) as file:
        s=file.next().replace("\n", "")
        ss=[float(a) for a in s.split(":")]
        datetime.timedelta(hours=ss[0], minutes=ss[1], seconds=ss[2])
        bb=datetime.timedelta(hours=ss[0], minutes=ss[1], seconds=ss[2])
        return bb.seconds+1.0*bb.microseconds/1000000
lrTimeList=list()
lrfhTimeList=list()
semTimeList=list()
ssemTimeList=list()
dayList=["2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
for day in dayList:
    lrTime=getTime("/home/chaowang/lr/offlineTime/log/season2/"+day+".log")
    lrfhTime=getTime("/home/chaowang/lr_fh/offlineTime/log/season2/"+day+".log")
    semTime=getTime("/home/chaowang/sem/offlineTime/log/season2/"+day+"/30.log")
    ssemTime=getTime("/home/chaowang/ssem/offlineTime/log/season2/"+day+"/30.log")
    lrTimeList.append(lrTime)
    lrfhTimeList.append(lrfhTime)
    semTimeList.append(semTime)
    ssemTimeList.append(ssemTime)
with open("./data/e14_a.dat", "w") as file:
	for i, lrTime, lrfhTime, semTime, ssemTime in zip(range(len(dayList)), lrTimeList, lrfhTimeList, semTimeList, ssemTimeList):
		file.write("%d %f %f %f %f\n"%(i, lrTime, lrfhTime, semTime, ssemTime))
lrTimeList=list()
lrfhTimeList=list()
semTimeList=list()
ssemTimeList=list()
dayList=["2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
for day in dayList:
    lrTime=getTime("/home/chaowang/lr/offlineTime/log/season3/"+day+".log")
    lrfhTime=getTime("/home/chaowang/lr_fh/offlineTime/log/season3/"+day+".log")
    semTime=getTime("/home/chaowang/sem/offlineTime/log/season3/"+day+"/40.log")
    ssemTime=getTime("/home/chaowang/ssem/offlineTime/log/season3/"+day+"/40.log")
    lrTimeList.append(lrTime)
    lrfhTimeList.append(lrfhTime)
    semTimeList.append(semTime)
    ssemTimeList.append(ssemTime)
with open("./data/e14_b.dat", "w") as file:
	for i, lrTime, lrfhTime, semTime, ssemTime in zip(range(len(dayList)), lrTimeList, lrfhTimeList, semTimeList, ssemTimeList):
		file.write("%d %f %f %f %f\n"%(i, lrTime, lrfhTime, semTime, ssemTime))
