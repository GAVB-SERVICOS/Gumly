# ref: https://github.com/gavbdheiver/predictive-maintenance-accelerator-/blob/main/predictive-maintenance-accelerator/Feature%20selection/Feat_Selection_Com_Stepwise/RUL_OPTUNA_DB4_Stepwise_Regression.ipynb
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.ensemble import RandomForestRegressor
import optuna
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.metrics import explained_variance_score, max_error
from sklearn.metrics import mean_squared_log_error, median_absolute_error


def model_function(model_name, parameters_dict):
    model = model_name(**parameters_dict)
    
    return model

#TODO : implement tuning_type with more methods
def tuning_hyperparam(df, parameters, model_name, n_trials):
    x, y = select_data(df, target)

    parameters_dict = {}
    def objective(trial):

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