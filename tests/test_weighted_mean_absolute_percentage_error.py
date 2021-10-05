import numpy as np
import pandas as pd
from mlutils.weighted_mean_absolute_percentage_error import * 


def test_wmap():

    y_true = pd.DataFrame(np.random.rand(6,5))
    y_pred = pd.DataFrame(np.random.rand(6,5))

    resultado = weighted_mean_absolute_percentage_error(y_true, y_pred)
    
    return print(resultado)

test_wmap()