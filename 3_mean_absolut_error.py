
def mean_absolute_error(y_true, y_pred):
    """
    Implements the MAE metric.
    Parameters:
                y_true - true target values
                y_pred - predicted target values
    Output:
                mae - mean absolute error
    """


    y_true = np.asarray(y_true).reshape(-1)
    y_pred = np.asarray(y_pred).reshape(-1)

    assert y_true.shape == y_pred.shape, "Predicted and true values have different shapes."
        
    mae = np.mean(np.abs(y_true-y_pred))
    
    return mae