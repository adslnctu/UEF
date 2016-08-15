import numpy as np
import sys, os
from sklearn.metrics import roc_curve, auc, log_loss
def getBest(dirname, k):
	aucList=list()
	loglossList=list()
	for filename in os.listdir(dirname):
		if filename.endswith(str(k)+".log"):
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
modelList=["UEF_Complex", "UEF_Simple"]
kList=[1, 10, 20, 30, 40, 50, 100]
smecXAUCList=list()
smecXLoglossList=list()
smecnoXAUCList=list()
smecnoXLoglossList=list()
dayList=["2013-06-07", "2013-06-08", "2013-06-09", "2013-06-10", "2013-06-11", "2013-06-12"]
for k in kList:
	smecXAUCSum=0.0
	smecXLoglossSum=0.0
	smecnoXAUCSum=0.0
	smecnoXLoglossSum=0.0
	for day in dayList:
		smecXAUC, smecXLogloss=getBest("/home/chaowang/sem/standard/log/season2/"+day+"/", k)
		smecXAUCSum+=smecXAUC
		smecXLoglossSum+=smecXLogloss
		smecnoXAUC, smecnoXLogloss=getBest("/home/chaowang/ssem/standard/log/season2/"+day+"/", k)
		smecnoXAUCSum+=smecnoXAUC
		smecnoXLoglossSum+=smecnoXLogloss
	smecXAUCList.append(smecXAUCSum/len(dayList))
	smecXLoglossList.append(smecXLoglossSum/len(dayList))
	smecnoXAUCList.append(smecnoXAUCSum/len(dayList))
	smecnoXLoglossList.append(smecnoXLoglossSum/len(dayList))
with open("./data/e2_a.dat", "w") as file:
	for k, smecXAUC, smecnoXAUC in zip(kList, smecXAUCList, smecnoXAUCList):
		file.write("%d %f %f\n"%(k, smecXAUC, smecnoXAUC))
with open("./data/e3_a.dat", "w") as file:
	for k, smecXLogloss, smecnoXLogloss in zip(kList, smecXLoglossList, smecnoXLoglossList):
		file.write("%d %f %f\n"%(k, smecXLogloss, smecnoXLogloss))
modelList=["UEF_Complex", "UEF_Simple"]
kList=[1, 10, 20, 30, 40, 50, 100]
smecXAUCList=list()
smecXLoglossList=list()
smecnoXAUCList=list()
smecnoXLoglossList=list()
dayList=["2013-10-20", "2013-10-21", "2013-10-22", "2013-10-23", "2013-10-24", "2013-10-25", "2013-10-26", "2013-10-27"]
for k in kList:
	smecXAUCSum=0.0
	smecXLoglossSum=0.0
	smecnoXAUCSum=0.0
	smecnoXLoglossSum=0.0
	for day in dayList:
		smecXAUC, smecXLogloss=getBest("/home/chaowang/sem/standard/log/season3/"+day+"/", k)
		smecXAUCSum+=smecXAUC
		smecXLoglossSum+=smecXLogloss
		smecnoXAUC, smecnoXLogloss=getBest("/home/chaowang/ssem/standard/log/season3/"+day+"/", k)
		smecnoXAUCSum+=smecnoXAUC
		smecnoXLoglossSum+=smecnoXLogloss
	smecXAUCList.append(smecXAUCSum/len(dayList))
	smecXLoglossList.append(smecXLoglossSum/len(dayList))
	smecnoXAUCList.append(smecnoXAUCSum/len(dayList))
	smecnoXLoglossList.append(smecnoXLoglossSum/len(dayList))
with open("./data/e2_b.dat", "w") as file:
	for k, smecXAUC, smecnoXAUC in zip(kList, smecXAUCList, smecnoXAUCList):
		file.write("%d %f %f\n"%(k, smecXAUC, smecnoXAUC))
with open("./data/e3_b.dat", "w") as file:
	for k, smecXLogloss, smecnoXLogloss in zip(kList, smecXLoglossList, smecnoXLoglossList):
		file.write("%d %f %f\n"%(k, smecXLogloss, smecnoXLogloss))
