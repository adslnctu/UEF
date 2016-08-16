#Overview
##Library
* [lib](./lib)  
    * [classifier](./lib/classifier): CTR prediction models
    * [featureDistribution](./lib/featureDistribution): Count conditional mean for each hashed feature 
    * [featureHasher](./lib/featureHasher): A streaming feature hasher dealing with nested dict based on [sklearn FeatureHasher](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.FeatureHasher.html)
    * [featureSelector](./lib/featureSelector)
    * [fileDB](./lib/fileDB)

##Experiment  
* [lr](./lr)
    * [offlineMemory](./lr/offlineMemory), [offlineTime](./lr/offlineTime), [onlineMemory](./lr/onlineMemory), [onlineTime](./lr/onlineTime), [standard](./lr/standard)
* [lr_fh](./lr_fh)
    * [offlineMemory](./lr_fh/offlineMemory), [offlineTime](./lr_fh/offlineTime), [onlineMemory](./lr_fh/onlineMemory), [onlineTime](./lr_fh/onlineTime), [standard](./lr_fh/standard)
* [ftrlProximal](./ftrlProximal)
    * [onlineMemory](./ftrlProximal/onlineMemory), [onlineTime](./ftrlProximal/onlineTime), [standard](./ftrlProximal/standard)
* [sem](./sem)
    * [offlineMemory](./sem/offlineMemory), [offlineTime](./sem/offlineTime), [onlineMemory](./sem/onlineMemory), [onlineTime](./sem/onlineTime), [standard](./sem/standard)
* [sem](./ssem)
    * [offlineMemory](./ssem/offlineMemory), [offlineTime](./ssem/offlineTime), [onlineMemory](./ssem/onlineMemory), [onlineTime](./ssem/onlineTime), [standard](./ssem/standard)

##Plot Data
* [plot](./plot)
