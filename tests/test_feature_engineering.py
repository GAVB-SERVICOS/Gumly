import numpy as np
import pandas as pd
import pytest
from sklearn import datasets

from gumly.feature_engineering import *


def test_feature_engineering_split_features_and_target():

    boston_data = datasets.load_boston()
    df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    df_boston["target"] = boston_data.target

    x, y = split_features_and_target(df_boston, "target")
    assert isinstance(x, pd.DataFrame)
    assert isinstance(y, pd.Series)


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

    assert feature_selection_wrapper(df_iris, "target", 3, 3) == [
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


def test_of():

    df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"])

    assert ordering_filter(df2, "a", lower_percentile=0.4, upper_percentile=0.1) == [
        0,
        2,
    ]

def test_drop_columns_with_null_threshold():

    df_input = pd.DataFrame(
        [
            ('Jack', np.NaN, 34, 'Sydney', np.NaN, 5, np.NaN, np.NaN, np.NaN),
            ('Riti', 23, 31, 'Delhi', np.NaN, 7, np.NaN, np.NaN, np.NaN),
            ('Aadi', np.NaN, 16, 'London', 32, 11, np.NaN, 3, np.NaN),
            ('Mark', np.NaN, 41, 'Delhi', np.NaN, 12, np.NaN, 11, 1),
        ],
        columns=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'],
    )

    df_out = drop_columns_with_null_threshold(df_input, 0.75)

    df_expected = pd.DataFrame(
        [
            ('Jack', 34, 'Sydney', 5, np.NaN),
            ('Riti', 31, 'Delhi', 7, np.NaN),
            ('Aadi', 16, 'London', 11, 3),
            ('Mark', 41, 'Delhi', 12, 11),
        ],
        columns=['A', 'C', 'D', 'F', 'H'],
    )

    pd.testing.assert_frame_equal(df_out, df_expected)
