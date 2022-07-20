import pandas as pd
import numpy as np
from imblearn.over_sampling import RandomOverSampler


def oversampler(X, y, method: str, sampling_strategy:str = 'auto', random_state=None, n_neighbors=5):
    """TODO:"""
    if "random" == method:
        sampler = RandomOverSampler(sampling_strategy=sampling_strategy, random_state=random_state)
    # elif "smote" == method:
    else:
        raise Exception(f"Method '{method}' not implemented!")
    
    return sampler.fit_resample(X, y)

