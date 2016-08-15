import numpy as np
import sys, os
from sklearn.metrics import roc_curve, auc, log_loss
def getMem(filename):
	with open(filename, "r") as file:
		for line in file:
			mem=float(line.replace("\n", ""))
	return mem
lrMemList=list()
lrfhMemList=list()
ftrlMemList=list()
semMemList=list()
ssemMemList=list()
dayList=["2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
for day in dayList:
	lrMem=getMem("/home/chaowang/lr/onlineMemory/log/season2/"+day+".log")
	lrfhMem=getMem("/home/chaowang/lr_fh/onlineMemory/log/season2/"+day+".log")
	ftrlMem=getMem("/home/chaowang/ftrlProximal/onlineMemory/log/season2/"+day+".log")
	semMem=getMem("/home/chaowang/sem/onlineMemory/log/season2/"+day+"/30.log")
	ssemMem=getMem("/home/chaowang/ssem/onlineMemory/log/season2/"+day+"/30.log")
	lrMemList.append(lrMem)
	lrfhMemList.append(lrfhMem)
	ftrlMemList.append(ftrlMem)
	semMemList.append(semMem)
	ssemMemList.append(ssemMem)
with open("./data/e4_a.dat", "w") as file:
	for i, lrMem, lrfhMem, ftrlMem, semMem, ssemMem in zip(range(len(dayList)), lrMemList, lrfhMemList, ftrlMemList, ssemMemList, ssemMemList):
		file.write("%d %f %f %f %f %f\n"%(i, lrMem, lrfhMem, ftrlMem, semMem, ssemMem))

lrMemList=list()
lrfhMemList=list()
ftrlMemList=list()
semMemList=list()
ssemMemList=list()
dayList=["2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
for day in dayList:
	lrMem=getMem("/home/chaowang/lr/onlineMemory/log/season3/"+day+".log")
	lrfhMem=getMem("/home/chaowang/lr_fh/onlineMemory/log/season3/"+day+".log")
	ftrlMem=getMem("/home/chaowang/ftrlProximal/onlineMemory/log/season3/"+day+".log")
	semMem=getMem("/home/chaowang/sem/onlineMemory/log/season3/"+day+"/40.log")
	ssemMem=getMem("/home/chaowang/ssem/onlineMemory/log/season3/"+day+"/40.log")
	lrMemList.append(lrMem)
	lrfhMemList.append(lrfhMem)
	ftrlMemList.append(ftrlMem)
	semMemList.append(semMem)
	ssemMemList.append(ssemMem)
with open("./data/e4_b.dat", "w") as file:
	for i, lrMem, lrfhMem, ftrlMem, semMem, ssemMem in zip(range(len(dayList)), lrMemList, lrfhMemList, ftrlMemList, ssemMemList, ssemMemList):
		file.write("%d %f %f %f %f %f\n"%(i, lrMem, lrfhMem, ftrlMem, semMem, ssemMem))
