
from mlutils.weighted_mean_absolute_percentage_error import * 


def test_wmap():

    y_true = [3, -0.5, 2, 7]
    y_pred = [2.5, 0.0, 2, 8]

    resultado = weighted_mean_absolute_percentage_error(y_true, y_pred)
    
    assert weighted_mean_absolute_percentage_error(y_true, y_pred) == 0.17391304347826086
    assert weighted_mean_absolute_percentage_error(y_true, y_pred) == 0.2

    return resultado