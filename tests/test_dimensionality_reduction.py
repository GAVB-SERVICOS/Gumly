import pandas as pd
import numpy as np
from scipy.sparse import csc_matrix
from mlutils.dimensionality_reduction import *


def test_svd():

    df = csc_matrix([[1, 0, 0], [5, 0, 2], [0, -1, 0], [0, 0, 3]], dtype=float)
    u, s, vt = svds(df, k=2)
    
    assert dimensionality_reduction(df, decomposition_method='SVD', k=2) == 
    
    return u

test_svd()

def test_pca():

    df = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    u = PCA(n_components=4, svd_solver='arpack').fit_transform(df.values)
    
    return u

test_pca()