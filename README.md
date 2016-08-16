#Overview
##Library
* [lib](./lib)  
    * [classifier](./lib/classifier): CTR prediction models
    * [featureDistribution](./lib/featureDistribution): Count conditional mean for each hashed feature 
    * [featureHasher](./lib/featureHasher): A streaming feature hasher dealing with nested dict based on [sklearn FeatureHasher](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html)
    * [featureSelector](./lib/featureSelector)
        * [poissonInclusion.py](./lib/featureSelector/poissonInclusion.py)
        * [significantFeatureSelector.py](./lib/featureSelector/significantFeatureSelector.py): select feature using featureDistribution
    * [fileDB](./lib/fileDB): read data

##Experiment
<img src="./Competitors.png" width="500">
* [lr](./lr): LR
    * [offlineMemory](./lr/offlineMemory), [offlineTime](./lr/offlineTime), [onlineMemory](./lr/onlineMemory), [onlineTime](./lr/onlineTime), [standard](./lr/standard)
* [lr_fh](./lr_fh): LR_FH
    * [offlineMemory](./lr_fh/offlineMemory), [offlineTime](./lr_fh/offlineTime), [onlineMemory](./lr_fh/onlineMemory), [onlineTime](./lr_fh/onlineTime), [standard](./lr_fh/standard)
* [ftrlProximal](./ftrlProximal): FTRL-Proximal
    * [onlineMemory](./ftrlProximal/onlineMemory), [onlineTime](./ftrlProximal/onlineTime), [standard](./ftrlProximal/standard)
* [sem](./sem): UEF_SEM
    * [offlineMemory](./sem/offlineMemory), [offlineTime](./sem/offlineTime), [onlineMemory](./sem/onlineMemory), [onlineTime](./sem/onlineTime), [standard](./sem/standard)
* [sem](./ssem): UEF_SSEM
    * [offlineMemory](./ssem/offlineMemory), [offlineTime](./ssem/offlineTime), [onlineMemory](./ssem/onlineMemory), [onlineTime](./ssem/onlineTime), [standard](./ssem/standard)

\# standord: evaluate AUC and Loglikelihood for the model

##Plot Data
* [plot](./plot)
   * [plot](./plot/e1.py)
   * [plot](./plot/e2_e3.py)
   * [plot](./plot/e1.py)
   * [plot](./plot/e1.py)
   * [plot](./plot/e1.py)
   * [plot](./plot/e1.py)
   * [plot](./plot/e1.py)
   * [plot](./plot/e1.py)
   * [plot](./plot/e1.py)
   * [plot](./plot/e1.py)
   * [plot](./plot/e1.py)
