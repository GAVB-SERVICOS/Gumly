import pandas as pd
import numpy as np
from scipy.sparse import csc_matrix
from mlutils.dimensionality_reduction import *
from numpy.testing import assert_almost_equal
import pytest


def test_dimensionality_reduction_svd():

    df = np.array(
        [
            [-1, -1, 2, -2],
            [-2, -1, 3, -1],
            [-3, -2, 5, 1],
            [1, 1, 6, 1],
            [2, 1, 7, 1],
            [3, 2, 8, 1],
        ],
    )
    n_array = np.array(
        [
            [0.34073313, 0.10864144],
            [0.47650997, 0.17692445],
            [0.70110855, 0.31684481],
            [-0.0675579, 0.44724498],
            [-0.17133298, 0.52770822],
            [-0.36244574, 0.61481713],
        ]
    )
    result = dimensionality_reduction(df, decomposition_method="SVD", k=2)
    print(type(result))
    assert_almost_equal(result, n_array)


def test_dimensionality_reduction_pca():

    df = np.array(
        [
            [-1, -1, 2, -2],
            [-2, -1, 3, -1],
            [-3, -2, 5, 1],
            [1, 1, 6, 1],
            [2, 1, 7, 1],
            [3, 2, 8, 1],
        ]
    )
    n_array = np.array(
        [
            [-3.55416303, -2.01120392],
            [-3.29181646, -0.37102401],
            [-2.55517195, 2.67830462],
            [1.76504972, 0.04940415],
            [2.9974995, 0.00646722],
            [4.63860223, -0.35194805],
        ]
    )
    result = dimensionality_reduction(df, k=2, decomposition_method="PCA")
    print(result)
    assert_almost_equal(result, n_array)


def test_dimensionality_reduction_valuerror():
    with pytest.raises(ValueError) as ex:
        df = np.array(
            [
                [-1, -1, 2, -2],
                [-2, -1, 3, -1],
                [-3, -2, 5, 1],
                [1, 1, 6, 1],
                [2, 1, 7, 1],
                [3, 2, 8, 1],
            ],
        )
        dimensionality_reduction(df, k=None, decomposition_method="PCA", explained_variance=None)
        assert ex.message == "k and explained_variance must be defined"


def test_dimensionality_reduction_typeerror():
    explained_variance = 1
    with pytest.raises(TypeError) as ex:
        df = np.array(
            [
                [-1, -1, 2, -2],
                [-2, -1, 3, -1],
                [-3, -2, 5, 1],
                [1, 1, 6, 1],
                [2, 1, 7, 1],
                [3, 2, 8, 1],
            ],
        )
        dimensionality_reduction(
            df,
            k=None,
            decomposition_method="PCA",
            explained_variance=explained_variance,
        )
        assert ex.message == f"explained_variance must be a float, but its value passed was {explained_variance}."


def test_dimensionality_reduction_valueerror():
    with pytest.raises(ValueError) as ex:
        df = np.array(
            [
                [-1, -1, 2, -2],
                [-2, -1, 3, -1],
                [-3, -2, 5, 1],
                [1, 1, 6, 1],
                [2, 1, 7, 1],
                [3, 2, 8, 1],
            ],
        )
        dimensionality_reduction(df, decomposition_method="PCA", explained_variance=1.9)
        assert ex.message == "explained_variance must be in the interval (0..1)"


def test_dimensionality_reduction_notimplementederror():
    with pytest.raises(NotImplementedError) as ex:
        df = np.array(
            [
                [-1, -1, 2, -2],
                [-2, -1, 3, -1],
                [-3, -2, 5, 1],
                [1, 1, 6, 1],
                [2, 1, 7, 1],
                [3, 2, 8, 1],
            ],
        )
        dimensionality_reduction(df, decomposition_method=None, explained_variance=0.2)
        assert ex.message == "Model implemented yet. Available names: 'SVD', 'PCA'."
