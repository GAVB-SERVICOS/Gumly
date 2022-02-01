from typing import Any, Dict, List

import optuna
import pandas as pd
from optuna.samplers import RandomSampler
from sklearn.metrics import make_scorer
from sklearn.model_selection import KFold, cross_val_score

from gumly.feature_engineering import split_features_and_target


def hyperparameter_tuning(
    df: pd.DataFrame,
    target: str,
    parameters: List[Dict[Any, Any]],
    algorithm,
    metric,
    metric_type,
    scoring_option: str,
    n_trials: int,
    n_splits: int,
    shuffle: bool,
    random_state: int,
    metric_goal: bool,
):

    """
    Perform hyperparameters optimization using optuna framework for the chosen technique.

    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param parameters: list that contains all the threshold given for optimization testing
    :type: List[Dict[Any, Any]]
    :param algorithm: Machine Learning algorithm used for fit the model
    (eg: RandomForestClassifier, RandomForestRegressor)
    :type: class
    :param metric: Metric used for the evaluation of the tests (eg: accuracy_score, r2)
    :type: function
    :param metric_type: Set 'Regression' for Regression metrics or 'Classification' for Classification metrics
    :type: str
    :param scoring_option: Maximize or minimize objectives
    :type: str
    :param n_trials: The of trials that the framework must perform
    :type: int
    :param n_splits: The number of splits that must be done in the dataset
    :type: int
    :param shuffle: The flag True or False for shuffle data before execution
    :type: bool
    :param random_state: The number choosen for seed
    :type: int
    :param metric_goal: If scoring_option is maximize, then set as True. Otherwise, set as False
    :type: int
    :return: Report as DataFrame, best value (metric) and best hyperparameter features chosen by the technique
    :rtype: DataFrame, float, dict

    """

    def objective(trial):

        parameters_dict = {}

        if parameters:
            for i, param in enumerate(parameters):
                if param["type"] == "Real":
                    parameters_dict[param["name"]] = trial.suggest_uniform(
                        name=param["name"], low=param["low"], high=param["high"]
                    )
                elif param["type"] == "Categorical":
                    parameters_dict[param["name"]] = trial.suggest_categorical(
                        name=param["name"], choices=param["choices"]
                    )

                elif param["type"] == "Integer":
                    parameters_dict[param["name"]] = trial.suggest_int(
                        name=param["name"], low=param["low"], high=param["high"]
                    )
                else:
                    raise NotImplementedError("Not implemented yet")

        my_model = algorithm(**parameters_dict)
        cv = KFold(n_splits=n_splits, shuffle=shuffle, random_state=random_state)
        metric_cv = cross_val_score(
            estimator=my_model, X=x, y=y, scoring=make_scorer(metric, greater_is_better=metric_goal), cv=cv
        )

        result = metric_cv.mean()

        if metric_type == 'Regression':
            return result

        elif metric_type == 'Classification':
            return 1.0 - result

    x, y = split_features_and_target(df=df, target=target)

    study = optuna.create_study(direction=scoring_option, sampler=RandomSampler(seed=random_state))
    study.optimize(objective, n_trials=n_trials)

    report_df = study.trials_dataframe(attrs=('number', 'value', 'params', 'state'))
    best_value = study.best_value
    best_param = study.best_params

    return report_df, best_value, best_param
