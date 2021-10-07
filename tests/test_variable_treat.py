import pandas as pd
from mlutils.variable_treat import *


def test_vt():
    
    data = pd.read_csv('aluguel.csv', sep = ';')
    
    result = variable_treat(data, 'Condominio', lower = True, lower_percentile=1.0, upper=True, upper_percentile=90.0)

    return result

test_vt()


