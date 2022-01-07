from sklearn import datasets
import pandas as pd

from mlutils.hyperparameter_tuning import *
from mlutils.feature_engineering import *
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import explained_variance_score, max_error
from sklearn.metrics import mean_squared_log_error, median_absolute_error
from sklearn.metrics import accuracy_score


def test_hyperparameter_tuning():

    iris_data = datasets.load_iris()
    df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df_iris["target"] = iris_data.target

    param_RF = [
        {"name": "min_samples_leaf", "type": "Integer", "low": 50, "high": 75},
        {"name": "max_depth", "type": "Integer", "low": 12, "high": 24},
    ]

    assert (
        type(
            hyperparameter_tuning(
                df=df_iris,
                target="target",
                parameters=param_RF,
                algorithm=RandomForestClassifier,
                metric=accuracy_score,
                scoring_option="maximize",
                n_trials=10,
            )
        )
        == dict
    )
