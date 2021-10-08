import pandas as pd
import numpy as np
from scipy.sparse import csc_matrix
from mlutils.dimensionality_reduction import *


def test_svd():

    df = np.array([[-1, -1, 2, -2], [-2, -1, 3, -1], [-3, -2, 5, 1], [1, 1, 6, 1], [2, 1, 7, 1], [3, 2, 8, 1]]).astype(np.float)
    n_array = np.array([[-0.34073313, -0.10864144],
       [-0.47650997, -0.17692445],
       [-0.70110855, -0.31684481],
       [ 0.0675579 , -0.44724498],
       [ 0.17133298, -0.52770822],
       [ 0.36244574, -0.61481713]])
    result = dimensionality_reduction(df, decomposition_method="SVD", k=2)
    print(type(result))
    assert np.array_equal(result, n_array )
    return result


test_svd()


"""
def test_pca():

    df = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    u = PCA(n_components=2).fit_transform(df)
    assert dimensionality_reduction(df,decomposition_method ='PCA', explained_variance=0.1) == [0.9924, 0.0075]
    return u

test_pca()
"""
