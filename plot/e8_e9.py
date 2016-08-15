import numpy as np
import sys, os
from sklearn.metrics import roc_curve, auc, log_loss
def getAUCLogloss(filename):
	with open(filename, "r") as file:
		allYList=list()
		allPList=list()	
		for line in file:
			line=line.replace("\n", "")
			ss=line.split(", ")
			if ss[len(ss)-2]=="True":
				allYList.append(True)
			else:
				allYList.append(False)
			if ss[len(ss)-1]=="None":
				q=0.5
			else:
				q=float(ss[len(ss)-1])
			allPList.append(q)
		fpr, tpr, thresholds=roc_curve(allYList, allPList)
		return auc(fpr, tpr), log_loss(allYList, allPList)
def getkBest(dirname, k):
	filenameList=list()
	aucList=list()
	loglossList=list()
	for filename in os.listdir(dirname):
		if filename.endswith(str(k)+".log"):
			filenameList.append(filename)
			with open(dirname+"/"+filename, "r") as file:
				try:
					allYList=list()
					allPList=list()
					for line in file:
						line=line.replace("\n", "")
						ss=line.split(", ")
						if ss[1]=="True":
							allYList.append(True)
						else:
							allYList.append(False)
						if ss[2]=="None":
							q=0.5
						else:
							q=float(ss[2])
						allPList.append(q)
					fpr, tpr, thresholds=roc_curve(allYList, allPList)
					a=auc(fpr, tpr)
					b=log_loss(allYList, allPList)
					aucList.append(a)
					loglossList.append(b)
				except ValueError:
					#print filename, "error"
					continue
				except :
					#print filename, "not finished"
					continue
	maxAUC=max(aucList)
	minLogloss=min(loglossList)
	return maxAUC, minLogloss
lrAUCList=list()
lrLoglossList=list()
lrfhAUCList=list()
lrfhLoglossList=list()
ftrlAUCList=list()
ftrlLoglossList=list()
semAUCList=list()
semLoglossList=list()
ssemAUCList=list()
ssemLoglossList=list()
dayList=["2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
for day in dayList:
	lrAUC, lrLogloss=getAUCLogloss("/home/chaowang/lr/standard/log/season2/"+day+".log")
	lrAUCList.append(lrAUC)
	lrLoglossList.append(lrLogloss)
	lrfhAUC, lrfhLogloss=getAUCLogloss("/home/chaowang/lr_fh/standard/log/season2/"+day+".log")
	lrfhAUCList.append(lrfhAUC)
	lrfhLoglossList.append(lrfhLogloss)
	ftrlAUC, ftrlLogloss=getAUCLogloss("/home/chaowang/ftrlProximal/standard/log/season2/"+day+"/0.03.log")
	ftrlAUCList.append(ftrlAUC)
	ftrlLoglossList.append(ftrlLogloss)
	semAUC, semLogloss=getkBest("/home/chaowang/sem/standard/log/season2/"+day+"/", 30)
	semAUCList.append(semAUC)
	semLoglossList.append(semLogloss)
	ssemAUC, ssemLogloss=getkBest("/home/chaowang/ssem/standard/log/season2/"+day+"/", 30)
	ssemAUCList.append(ssemAUC)
	ssemLoglossList.append(ssemLogloss)
with open("./data/e8_a.dat", "w") as file:
	for i, lrAUC, lrfhAUC, ftrlAUC, semAUC, ssemAUC in zip(range(len(dayList)), lrAUCList, lrfhAUCList, ftrlAUCList, semAUCList, ssemAUCList):
		file.write("%d %f %f %f %f %f\n"%(i, lrAUC, lrfhAUC, ftrlAUC, semAUC, ssemAUC))
with open("./data/e9_a.dat", "w") as file:
	for i, lrLogloss, lrfhLogloss, ftrlLogloss, semLogloss, ssemLogloss in zip(range(len(dayList)), lrLoglossList, lrfhLoglossList, ftrlLoglossList, semLoglossList, ssemLoglossList):
		file.write("%d %f %f %f %f %f\n"%(i, -lrLogloss, -lrfhLogloss, -ftrlLogloss, -semLogloss, -ssemLogloss))
lrAUCList=list()
lrLoglossList=list()
lrfhAUCList=list()
lrfhLoglossList=list()
ftrlAUCList=list()
ftrlLoglossList=list()
semAUCList=list()
semLoglossList=list()
ssemAUCList=list()
ssemLoglossList=list()
dayList=["2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
for day in dayList:
	lrAUC, lrLogloss=getAUCLogloss("/home/chaowang/lr/standard/log/season3/"+day+".log")
	lrAUCList.append(lrAUC)
	lrLoglossList.append(lrLogloss)
	lrfhAUC, lrfhLogloss=getAUCLogloss("/home/chaowang/lr_fh/standard/log/season3/"+day+".log")
	lrfhAUCList.append(lrfhAUC)
	lrfhLoglossList.append(lrfhLogloss)
	ftrlAUC, ftrlLogloss=getAUCLogloss("/home/chaowang/ftrlProximal/standard/log/season3/"+day+"/0.03.log")
	ftrlAUCList.append(ftrlAUC)
	ftrlLoglossList.append(ftrlLogloss)
	semAUC, semLogloss=getkBest("/home/chaowang/sem/standard/log/season3/"+day+"/", 40)
	semAUCList.append(semAUC)
	semLoglossList.append(semLogloss)
	ssemAUC, ssemLogloss=getkBest("/home/chaowang/ssem/standard/log/season3/"+day+"/", 40)
	ssemAUCList.append(ssemAUC)
	ssemLoglossList.append(ssemLogloss)
with open("./data/e8_b.dat", "w") as file:
	for i, lrAUC, lrfhAUC, ftrlAUC, semAUC, ssemAUC in zip(range(len(dayList)), lrAUCList, lrfhAUCList, ftrlAUCList, semAUCList, ssemAUCList):
		file.write("%d %f %f %f %f %f\n"%(i, lrAUC, lrfhAUC, ftrlAUC, semAUC, ssemAUC))
with open("./data/e9_b.dat", "w") as file:
	for i, lrLogloss, lrfhLogloss, ftrlLogloss, semLogloss, ssemLogloss in zip(range(len(dayList)), lrLoglossList, lrfhLoglossList, ftrlLoglossList, semLoglossList, ssemLoglossList):
		file.write("%d %f %f %f %f %f\n"%(i, -lrLogloss, -lrfhLogloss, -ftrlLogloss, -semLogloss, -ssemLogloss))
