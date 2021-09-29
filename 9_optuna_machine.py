#!pip install optuna
import optuna
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score


#def model_function(model_name, parameters_dict):
       
    #model = model_name(**parameters_dict)
    #model.fit(X_train, y_train)
    
    #return model




def optuna_machine(X_train, y_train, parameters, model_name, n_trials):
    
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
    
    
        # Generates validation data
        #X_train_o, X_val_o, y_train_o, y_val_o = train_test_split(X_train, y_train, test_size=validation_size, 
        #                                                            random_state=np.random.seed(42))
        # Train model and evaluates it on validation data
        my_model = model_function(model_name, parameters_dict) # Importa a função model_function anterior celula 22 #
        cv = KFold(shuffle= True, random_state=42)
        metric_cv = cross_val_score(my_model, X_train, y_train, cv=cv, scoring='neg_mean_squared_error')
    
        #y_pred_o = my_model.predict(X_val_o)
        #metric = mean_squared_error(y_true=y_val_o, y_pred=y_pred_o)
        metric = abs(metric_cv.mean())
    
        return metric

    print('Running optuna parameters/hyperparameters optimization...')
    study = optuna.create_study(direction='minimize')
    study.optimize(objective, n_trials=n_trials)

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