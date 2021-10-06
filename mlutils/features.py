# classification
from sklearn.linear_model import LogisticRegression


class classification:
    def __init__(self):

        self.x = x

    def _train(self, y, model):

        try:
            model.fit(x, y)
        except:
            print("Something went wrong at train step")
        else:
            return model

    def _predict(self, model_trained, type_predict):

        try:
            if type_predict == 0:
                results = model_trained.predict(x)

            elif type_predict == 1:
                results = model.predict_proba(x)
        except:
            print("Something went wrong")
        else:
            return results

    def run_train_models(self, list_models):

        try:
            for i in range(len(list_models)):
                model_[i] = _train(self, list_models[i])
                #TODO: terminar aqui
        except:
            print("Something went wrong at the run_train_models")
        else:
            print("Run models executed successfully")
