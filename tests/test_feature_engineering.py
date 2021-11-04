from sklearn import datasets
import pandas as pd
from mlutils.feature_engineering import *


def test_feature_engineering_select_data():
    iris_data = datasets.load_iris()
    df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df_iris["target"] = iris_data.target

    boston_data = datasets.load_boston()
    df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    df_boston["target"] = boston_data.target

    x_reg, y_reg = select_data(df_boston, "target")
    x_class, y_class = select_data(df_iris, "target")
    print("select_data OK!")



# classification
def test_feature_engineering_feature_selection_filter():
    
    iris_data = datasets.load_iris()
    df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df_iris["target"] = iris_data.target

    filter_result = feature_selection_filter(df=df_iris, target="target", num_feats=3)
    print("filter class OK!")



def test_feature_engineering_feature_selection_wrapper():
    iris_data = datasets.load_iris()
    df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df_iris["target"] = iris_data.target
    
    wrapper_result = feature_selection_wrapper(df_iris, "target", 3)
    print("wrapper OK!")


def test_feature_engineering_feature_selection_embedded():
    iris_data = datasets.load_iris()
    df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df_iris["target"] = iris_data.target

    embedded_result = feature_selection_embedded(df_iris, "target", 3)
    print("embedded OK!")



# regression
def test_feature_engineering_feature_selection_stepwise():
    
    boston_data = datasets.load_boston()
    df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    df_boston["target"] = boston_data.target
    
    step_result = feature_selection_stepwise(df_boston, "target", 0.01, 0.05, True)
    print("step wise OK!")

  
def test_feature_engineering_feature_selection_f_regression():
    
    boston_data = datasets.load_boston()
    df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    df_boston["target"] = boston_data.target  

    f_reg_result = feature_selection_f_regression(df_boston, "target", 3)
    print("f_regression OK!")


def test_feature_engineering_feature_selection_mutual_information():
    
    boston_data = datasets.load_boston()
    df_boston = pd.DataFrame(boston_data.data, columns=boston_data.feature_names)
    df_boston["target"] = boston_data.target 
 
    mutual_info_reg_result = feature_selection_mutual_information(
        df_boston, "target", 3
    )
    print("mutual info reg OK!")



