# From the module
from gumly.ibge import fetch
from gumly.ibge import city_to_region
from gumly.ibge import city_to_microregion
from gumly.ibge import city_to_mesoregion
from gumly.ibge import city_to_state
from gumly.ibge import state_to_region
from gumly.ibge import cep_to_state
from gumly.ibge import cep_to_region

# Others
import pandas as pd
from pandas.testing import assert_series_equal
import numpy as np


def test_city_to_region():
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  # With a typo on the last entry

    df = pd.DataFrame(data=d)

    ibge_data = {'municipios_regiao': {'saopaulo': 'Sudeste'}}

    espected = pd.Series(['Sudeste', 'Sudeste', 'Sudeste', np.nan], name='temp')

    result = city_to_region(df, 'City', ibge_data)

    assert_series_equal(result, espected, check_dtype=False, check_categorical=False)
