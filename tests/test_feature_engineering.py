import numpy as np
import pandas as pd
from sklearn import datasets

from gumly.feature_engineering import (
    feature_selection_embedded,
    feature_selection_f_regression,
    feature_selection_filter,
    feature_selection_mutual_information,
    feature_selection_stepwise,
    feature_selection_wrapper,
    ordering_filter,
    split_features_and_target,
)


def test_feature_engineering_split_features_and_target():

    boston_data = datasets.load_iris()
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

    diabetes_data = datasets.load_diabetes()
    df_diabetes = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
    df_diabetes["bp"] = diabetes_data.target

    assert feature_selection_stepwise(df_diabetes, "bp", 0.01, 0.05, False) == ["bmi", "s5", "s1"]


def test_feature_engineering_feature_selection_f_regression():

    diabetes_data = datasets.load_diabetes()
    df_diabetes = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
    df_diabetes["bp"] = diabetes_data.target

    assert feature_selection_f_regression(df_diabetes, "bp", 3) == [
        "bmi",
        "s4",
        "s5",
    ]


def test_feature_engineering_feature_selection_mutual_information():

    diabetes_data = datasets.load_diabetes()
    df_diabetes = pd.DataFrame(diabetes_data.data, columns=diabetes_data.feature_names)
    df_diabetes["bp"] = diabetes_data.target

    assert feature_selection_mutual_information(df_diabetes, "bp", 3) == [
        "bmi",
        "s5",
        "s6",
    ]


def test_of():

    df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"])

    assert ordering_filter(df2, "a", lower_percentile=0.4, upper_percentile=0.1) == [
        0,
        2,
    ]
