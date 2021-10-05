# ref: https://github.com/gavbdheiver/predictive-maintenance-accelerator-/blob/main/predictive-maintenance-accelerator/Feature%20selection/Feat_Selection_Com_Stepwise/RUL_OPTUNA_DB4_Stepwise_Regression.ipynb
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestRegressor
import optuna
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import explained_variance_score, max_error
from sklearn.metrics import mean_squared_log_error, median_absolute_error

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
    
    #print("Número de tentativas finalizadas: ", len(study.trials))
    #print("Melhor tentativa:")
    trial = study.best_trial
    #print("  Valor: {}".format(trial.value))
    #print("  Parâmetros: ")
    #for key, value in trial.params.items():
    #    print("    {}: {}".format(key, value))
        
    return study.best_params












# old


# FYI: Objective functions can take additional arguments
# (https://optuna.readthedocs.io/en/stable/faq.html#objective-func-additional-args).
def objective(trial):
    data, target = sklearn.datasets.load_breast_cancer(return_X_y=True)
    train_x, valid_x, train_y, valid_y = train_test_split(data, target, test_size=0.25)
    dtrain = xgb.DMatrix(train_x, label=train_y)
    dvalid = xgb.DMatrix(valid_x, label=valid_y)

    param = {
        "verbosity": 0,
        "objective": "binary:logistic",
        "eval_metric": "auc",
        "booster": trial.suggest_categorical("booster", ["gbtree", "gblinear", "dart"]),
        "lambda": trial.suggest_float("lambda", 1e-8, 1.0, log=True),
        "alpha": trial.suggest_float("alpha", 1e-8, 1.0, log=True),
    }

    if param["booster"] == "gbtree" or param["booster"] == "dart":
        param["max_depth"] = trial.suggest_int("max_depth", 1, 9)
        param["eta"] = trial.suggest_float("eta", 1e-8, 1.0, log=True)
        param["gamma"] = trial.suggest_float("gamma", 1e-8, 1.0, log=True)
        param["grow_policy"] = trial.suggest_categorical("grow_policy", ["depthwise", "lossguide"])
    if param["booster"] == "dart":
        param["sample_type"] = trial.suggest_categorical("sample_type", ["uniform", "weighted"])
        param["normalize_type"] = trial.suggest_categorical("normalize_type", ["tree", "forest"])
        param["rate_drop"] = trial.suggest_float("rate_drop", 1e-8, 1.0, log=True)
        param["skip_drop"] = trial.suggest_float("skip_drop", 1e-8, 1.0, log=True)

    # Add a callback for pruning.
    pruning_callback = optuna.integration.XGBoostPruningCallback(trial, "validation-auc")
    bst = xgb.train(param, dtrain, evals=[(dvalid, "validation")], callbacks=[pruning_callback])
    preds = bst.predict(dvalid)
    pred_labels = np.rint(preds)
    accuracy = sklearn.metrics.accuracy_score(valid_y, pred_labels)
    return accuracy


if __name__ == "__main__":
    study = optuna.create_study(
        pruner=optuna.pruners.MedianPruner(n_warmup_steps=5), direction="maximize"
    )
    study.optimize(objective, n_trials=100)
    print(study.best_trial)

    #--------------------------------------


def model_function(model_name, parameters_dict):
    model = model_name(**parameters_dict)
    
    return model

#TODO : implement tuning_type with more methods
def tuning_hyperparam(df, parameters, model_name, n_trials):
    x, y = select_data(df, target)

    parameters_dict = {}
    #def objective(trial):

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


    my_model = model_function(model_name, parameters_dict)
    cv = KFold(shuffle= True, random_state=42)
    metric_cv = cross_val_score(my_model, X_train, y_train, cv=cv, scoring='neg_mean_squared_error')
    metric = abs(metric_cv.mean())
    
    return metric

def run_tuning():
    study = optuna.create_study(direction='minimize')
    study.optimize(objective(trial), n_trials=n_trials)

    #sampler = optuna.samplers.TPESampler(seed=10)
    #optuna.visualization.matplotlib.plot_contour(study, params=parameters)
    
    print("Número de tentativas finalizadas: ", len(study.trials))
    print("Melhor tentativa:")
    trial = study.best_trial
    print("  Valor: {}".format(trial.value))
    print("  Parâmetros: ")
    for key, value in trial.params.items():
        print("    {}: {}".format(key, value))
        
    return study.best_params