import pandas as pd
import numpy as np
from mlutils.use_dimensionality_reduction import *


def test_svd():

    df = pd.DataFrame(np.random.rand(6,5))
    u, s, vt = svds(df, k=4)

    return u, s, vt

test_svd()

def test_pca():

    df = pd.DataFrame(np.random.rand(6,5))
    u = PCA(n_components=4, svd_solver='arpack').fit_transform(df.values)

    return u

test_pca()