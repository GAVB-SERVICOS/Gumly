# ref: https://github.com/gavbdheiver/predictive-maintenance-accelerator-/blob/main/predictive-maintenance-accelerator/Feature%20selection/Feat_Selection_Com_Stepwise/RUL_OPTUNA_DB4_Stepwise_Regression.ipynb
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
import optuna
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import explained_variance_score, max_error
from sklearn.metrics import mean_squared_log_error, median_absolute_error

from mlutils.feature_engineering import *

def tuning_hyperparams(df, target, parameters, algorithm, metric, scoring_option, n_trials):

    '''
    Perform hyperparameters optimization using optuna framework for the chosen technique.

    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param parameters: Dict that contains all the threshold given for optimization testing
    :type: dict
    :param algorithm: Machine Learning algorithm used for fit the model
    :type: str
    :param metric: Metric used for the evaluation of the tests
    :type: str
    :param scoring_option: Maximization or minimization objectives
    :type: str
    :param n_trials: The of trials that the framework must perform
    :type: int
    :raise exception: The optimization method couldn't be processed
    :return: Best hyperparameter features chosen by the technique 
    :rtype: dict

    '''

    x, y = select_data(df, target)

    parameters_dict = {}
    def objective(trial, metric):

        if parameters:   
            for i, param in enumerate(parameters):

                if param["type"] == "Real":  
                    parameters_dict[param["name"]] = trial.suggest_uniform(name=param["name"], 
                                                                                            low=param["low"], high=param["high"])
                elif param["type"] == "Categorical":
                    parameters_dict[param["name"]] = trial.suggest_categorical(name=param["name"], choices=param["choices"])

                elif param["type"] == "Integer":
                    parameters_dict[param["name"]] = trial.suggest_int(name=param["name"], 
                                                                                        low=param["low"], high=param["high"])
                else:
                    raise NotImplemented("Not implemented yet")


        my_model = algorithm(parameters_dict)
        cv = KFold(shuffle= True, random_state=42)
        metric_cv = cross_val_score(my_model, x, y, cv=cv, scoring=metric)

        metric = abs(metric_cv.mean())
    
        return metric

    study = optuna.create_study(direction=scoring_option)
    study.optimize(objective, n_trials=n_trials)
    trial = study.best_trial
        
    return study.best_params