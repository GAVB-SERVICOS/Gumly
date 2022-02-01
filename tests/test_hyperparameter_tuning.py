import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    explained_variance_score,
    max_error,
    mean_absolute_error,
    mean_squared_error,
    mean_squared_log_error,
    median_absolute_error,
    r2_score,
)

from gumly.feature_engineering import *
from gumly.hyperparameter_tuning import *


def test_hyperparameter_tuning():

    iris_data = datasets.load_iris()
    df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df_iris["target"] = iris_data.target

    param_RF = [
        {"name": "min_samples_leaf", "type": "Integer", "low": 50, "high": 75},
        {"name": "max_depth", "type": "Integer", "low": 1, "high": 12},
    ]

    r, v, p = hyperparameter_tuning(
        df=df_iris,
        target="target",
        parameters=param_RF,
        algorithm=RandomForestClassifier,
        metric=accuracy_score,
        metric_type='Classification',
        scoring_option="maximize",
        n_trials=1,
        n_splits=2,
        shuffle=True,
        random_state=42,
        metric_goal=True,
    )

    r2, v2, p2 = hyperparameter_tuning(
        df=df_iris,
        target="target",
        parameters=param_RF,
        algorithm=RandomForestClassifier,
        metric=accuracy_score,
        metric_type='Classification',
        scoring_option="maximize",
        n_trials=5,
        n_splits=2,
        shuffle=True,
        random_state=42,
        metric_goal=True,
    )

    assert v2 >= v
