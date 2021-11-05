from numpy.testing._private.utils import assert_almost_equal
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


def test_feature_engineering_feature_selection_mutual_information(): # Resultado variando

    boston_data = datasets.load_boston()
    df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    df_boston["target"] = boston_data.target

    assert feature_selection_mutual_information(df_boston, "target", 3) == [
        "INDUS",
        "RM",
        "LSTAT",
    ]


def test_feature_engineering_select_data_error_to_process():
    with pytest.raises(Exception) as ex:
        boston_data = datasets.load_boston()
        df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
        df_boston["target"] = boston_data.target
    
        select_data(df_boston, "tar")
        assert ex.message == "an error occured during DataFrame handling"


def test_feature_engineering_feature_selection_filter_error_to_process():
    with pytest.raises(Exception) as ex:
        iris_data = datasets.load_iris()
        df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
        df_iris["target"] = iris_data.target

        feature_selection_filter(df=df, target="tar", num_feats=3)
        assert ex.message == "An error occured during filter selection process"
        

def test_feature_engineering_feature_selection_wrapper_error_to_process():
    with pytest.raises(Exception) as ex:
        iris_data = datasets.load_iris()
        df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
        df_iris["target"] = iris_data.target
        feature_selection_wrapper(df_iris, "tar", 3)
        assert ex.message == "An error occured during wrapper selection process"

def test_feature_engineering_feature_selection_embedded_error_to_process():
    with pytest.raises(Exception) as ex:
        iris_data = datasets.load_iris()
        df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
        df_iris["target"] = iris_data.target

        feature_selection_embedded(df_iris, "tar", 3, 50)
        assert ex.message == "An error occured during embedded selection process"

def test_feature_engineering_feature_selection_stepwise_error_to_process():
    with pytest.raises(Exception) as ex:
        boston_data = datasets.load_boston()
        df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
        df_boston["target"] = boston_data.target

        feature_selection_stepwise(df_boston, "tar", 0.01, 0.05, False)
        assert ex.message == "An error occured during step wise selection process"

def test_feature_engineering_feature_selection_f_regression_error_to_process():
    with pytest.raises(Exception) as ex:
        boston_data = datasets.load_boston()
        df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
        df_boston["target"] = boston_data.target

        feature_selection_f_regression(df_boston, "tar", 3)   
        assert ex.message == "An error occured during f_regression selection process"

def test_feature_engineering_feature_selection_mutual_information_error_to_process(): # Resultado variando
    with pytest.raises(Exception) as ex:
        boston_data = datasets.load_boston()
        df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
        df_boston["target"] = boston_data.target

        feature_selection_mutual_information(df_boston, "target", 3)
        assert ex.message == "An error occured during mutual_info_regression selection process"    