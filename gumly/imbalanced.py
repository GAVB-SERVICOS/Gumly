import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN
from imblearn.under_sampling import RandomUnderSampler
from imblearn.under_sampling import NearMiss
from imblearn.under_sampling import TomekLinks

def oversampler(X, y, 
                method: str = 'random', 
                sampling_strategy: str = 'auto', 
                random_state=None, 
                n_neighbors=5):
    """TODO:
    
    """
    if "random" == method.lower():
        sampler = RandomOverSampler(sampling_strategy=sampling_strategy, 
                                    random_state=random_state)
    
    elif "smote" == method.lower():
        sampler = SMOTE(sampling_strategy=sampling_strategy, 
                        random_state=random_state, 
                        k_neighbors=n_neighbors)
    
    elif "adasyn" == method.lower():
        sampler = ADASYN(sampling_strategy=sampling_strategy, 
                         random_state=random_state, 
                         n_neighbors=n_neighbors)
    
    else:
        raise Exception(f"Method '{method}' not implemented!")
    
    return sampler.fit_resample(X, y)

def undersampler(X, y, 
                 method: str, 
                 sampling_strategy:str = 'auto', 
                 random_state=None, 
                 n_neighbors:int=3,
                 n_neighbors_ver3:int=3, 
                 replacement:bool=False, 
                 n_jobs:int=-1):
    """TODO:
    
    """
    if "random" == method.lower():
        sample = RandomUnderSampler(sampling_strategy=sampling_strategy,
                                     random_state=random_state,
                                     replacement=replacement,
                                    )
    elif "nearmiss" == method.lower():
        sample = NearMiss(sampling_strategy=sampling_strategy, 
                           n_neighbors=n_neighbors,
                           n_neighbors_ver3=n_neighbors_ver3,
                           n_jobs=n_jobs)
    elif "tomeklinks" == method.lower():
        sample = TomekLinks(sampling_strategy=sampling_strategy,
                             n_jobs=n_jobs)
    else:
        raise Exception(f"Method '{method}' not implemented!")    

    return sample.fit_resample(X, y)



#def combine(X, y, method: str, sampling_strategy:str = 'auto', random_state=None, n_neighbors=5):
#    """TODO:
#    
#    """
#    if "random" == method.lower():