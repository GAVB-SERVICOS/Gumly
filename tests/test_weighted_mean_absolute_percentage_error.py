import pytest
import numpy as np
import pandas as pd
from mlutils.weighted_mean_absolute_percentage_error import * 



def get_df(m, n):
    y = pd.DataFrame(np.random.rand(m,n))
    return y

def test_wmap(y_true, y_pred):

    resultado = weighted_mean_absolute_percentage_error(y_true, y_pred)
    return resultado


y_true = get_df(6,5)
y_pred = get_df(6,5)


print(test_wmap(y_true, y_pred))