from numpy.testing._private.utils import assert_almost_equal
import numpy as np
from sklearn import datasets
import pandas as pd
from mlutils.feature_engineering import *
import pytest


def test_feature_engineering_select_data():

    boston_data = datasets.load_boston()
    df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    df_boston["target"] = boston_data.target

    x, y = select_data(df_boston, "target")
    isinstance(x, pd.DataFrame)
    isinstance(y, pd.DataFrame)


# classification
def test_feature_engineering_feature_selection_filter():

    iris_data = datasets.load_iris()
    df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df_iris["target"] = iris_data.target

    assert feature_selection_filter(df=df_iris, target="target", num_feats=3) == [
        "sepal length (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]


def test_feature_engineering_feature_selection_wrapper():
    iris_data = datasets.load_iris()
    df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df_iris["target"] = iris_data.target

    assert feature_selection_wrapper(df_iris, "target", 3) == [
        "sepal width (cm)",
        "petal length (cm)",
        "petal width (cm)",
    ]


def test_feature_engineering_feature_selection_embedded():
    iris_data = datasets.load_iris()
    df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df_iris["target"] = iris_data.target

    assert feature_selection_embedded(df_iris, "target", 3, 50) == ["petal length (cm)"]


# regression
def test_feature_engineering_feature_selection_stepwise():

    boston_data = datasets.load_boston()
    df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    df_boston["target"] = boston_data.target

    assert feature_selection_stepwise(df_boston, "target", 0.01, 0.05, False) == [
        "LSTAT",
        "RM",
        "PTRATIO",
        "DIS",
        "NOX",
        "CHAS",
        "B",
        "ZN",
    ]


def test_feature_engineering_feature_selection_f_regression():

    boston_data = datasets.load_boston()
    df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    df_boston["target"] = boston_data.target

    assert feature_selection_f_regression(df_boston, "target", 3) == [
        "RM",
        "PTRATIO",
        "LSTAT",
    ]


def test_feature_engineering_feature_selection_mutual_information():

    boston_data = datasets.load_boston()
    df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    df_boston["target"] = boston_data.target

    assert feature_selection_mutual_information(df_boston, "target", 3) == [
        "INDUS",
        "RM",
        "LSTAT",
    ]



def test_vt():

    df2 = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"]
    )

    assert variable_treat(
        df2, "a", lower=True, lower_percentile=1.0, upper=True, upper_percentile=2.0
    ) == [0, 1, 2]


test_vt()


def test_passes():
    with pytest.raises(NotImplementedError) as ex:
        df2 = pd.DataFrame(
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"]
        )
        variable_treat(
            df2,
            "a",
            lower=False,
            lower_percentile=1.0,
            upper=False,
            upper_percentile=90.0,
        )
        assert ex.message == "One of those paramns must be True"