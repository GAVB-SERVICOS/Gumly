import pandas as pd
import numpy as np
from gumly.dimensionality_reduction import *
from numpy.testing import assert_almost_equal
import pytest


def test_dimensionality_reduction_svd():

    df = np.array(
        [[-1, -1, 2, -2], [-2, -1, 3, -1], [-3, -2, 5, 1], [1, 1, 6, 1], [2, 1, 7, 1], [3, 2, 8, 1],], dtype=float
    )

    v0 = np.ones(df.shape[-1])
    n_array, _, _ = svds(df, k=2, v0=v0)

    result = dimensionality_reduction(df, decomposition_method="SVD", k=2, v0=v0)

    assert_almost_equal(n_array, result)
    assert result.shape[1] == 2


def test_dimensionality_reduction_pca():

    df = np.array([[-1, -1, 2, -2], [-2, -1, 3, -1], [-3, -2, 5, 1], [1, 1, 6, 1], [2, 1, 7, 1], [3, 2, 8, 1],])

    n_array = PCA(2).fit_transform(df)

    result = dimensionality_reduction(df, k=2, decomposition_method="PCA")
    print(result)
    assert_almost_equal(result, n_array)
    assert result.shape[1] == 2


def test_dimensionality_reduction_valuerror():
    with pytest.raises(ValueError) as ex:
        df = np.array([[-1, -1, 2, -2], [-2, -1, 3, -1], [-3, -2, 5, 1], [1, 1, 6, 1], [2, 1, 7, 1], [3, 2, 8, 1],],)
        dimensionality_reduction(df, k=None, decomposition_method="PCA", explained_variance=None)
        assert ex.message == "k and explained_variance must be defined"


def test_dimensionality_reduction_typeerror():
    explained_variance = 1
    with pytest.raises(TypeError) as ex:
        df = np.array([[-1, -1, 2, -2], [-2, -1, 3, -1], [-3, -2, 5, 1], [1, 1, 6, 1], [2, 1, 7, 1], [3, 2, 8, 1],],)
        dimensionality_reduction(
            df, k=None, decomposition_method="PCA", explained_variance=explained_variance,
        )
        assert ex.message == f"explained_variance must be a float, but its value passed was {explained_variance}."


def test_dimensionality_reduction_valueerror():
    with pytest.raises(ValueError) as ex:
        df = np.array([[-1, -1, 2, -2], [-2, -1, 3, -1], [-3, -2, 5, 1], [1, 1, 6, 1], [2, 1, 7, 1], [3, 2, 8, 1],],)
        dimensionality_reduction(df, decomposition_method="PCA", explained_variance=1.9)
        assert ex.message == "explained_variance must be in the interval (0..1)"


def test_dimensionality_reduction_notimplementederror():
    with pytest.raises(NotImplementedError) as ex:
        df = np.array([[-1, -1, 2, -2], [-2, -1, 3, -1], [-3, -2, 5, 1], [1, 1, 6, 1], [2, 1, 7, 1], [3, 2, 8, 1],],)
        dimensionality_reduction(df, decomposition_method=None, explained_variance=0.2)
        assert ex.message == "Model implemented yet. Available names: 'SVD', 'PCA'."
