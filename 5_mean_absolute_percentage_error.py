import numpy as np # Existe biblioteca


def mean_absolute_percentage_error(y_true, y_pred):
    """Implements the MAPE metric.
       Parameters:
                  y_true - true target values
                  y_pred - predicted target values
       Output:    mean absolute percentage error
    
    """

    y_true = np.asarray(y_true).reshape(-1)
    y_pred = np.asarray(y_pred).reshape(-1)

    assert y_true.shape == y_pred.shape, "Predicted and true values have different shapes."
    
    
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100
