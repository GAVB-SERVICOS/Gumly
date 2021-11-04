from sklearn import datasets
import pandas as pd

from mlutils.tuning_hyperparams import *
from mlutils.feature_engineering import *
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import explained_variance_score, max_error
from sklearn.metrics import mean_squared_log_error, median_absolute_error


def test_tuning_hyperparams():

    iris_data = datasets.load_iris()
    df_iris = pd.DataFrame(data=iris_data.data, columns=iris_data.feature_names)
    df_iris["target"] = iris_data.target

    param_RF = [
        {"name": "min_samples_leaf", "type": "Integer", "low": 50, "high": 75},
        {"name": "max_depth", "type": "Integer", "low": 12, "high": 24},
    ]
    #import pdb
    #pdb.set_trace()

    # tuning_hyperparams(df, target, parameters, algorithm, metric, scoring_option, n_trials)
    assert tuning_hyperparams(
        df=df_iris,
        target="target",
        parameters=param_RF,
        algorithm=RandomForestClassifier,
        metric=r2_score,
        scoring_option="maximize",
        n_trials=10,
    ) == {'min_samples_leaf': 57, 'max_depth': 18}
