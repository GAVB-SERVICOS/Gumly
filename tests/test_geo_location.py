# From the module
from gumly.geo_location import city_to_imediate_region, city_to_intermediarie_region, fetch
from gumly.geo_location import city_to_region
from gumly.geo_location import city_to_microregion
from gumly.geo_location import city_to_mesoregion
from gumly.geo_location import city_to_state
from gumly.geo_location import state_to_region
from gumly.geo_location import cep_to_state
from gumly.geo_location import cep_to_region

# Others
import pandas as pd
from pandas.testing import assert_series_equal
import numpy as np


def test_city_to_region():
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    ibge_data = {'municipios_regiao': {'saopaulo': 'Sudeste'}}

    expected = pd.Series(['Sudeste', 'Sudeste', 'Sudeste', np.nan], name='temp')

    result = city_to_region(df, 'City', ibge_data)

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


def test_city_to_microregion():
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    ibge_data = {'municipios_microrregiao': {'saopaulo': 'São Paulo'}}

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_microregion(df, 'City', ibge_data)

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


def test_city_to_mesoregion():
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    ibge_data = {'municipios_mesorregiao': {'saopaulo': 'São Paulo'}}

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_mesoregion(df, 'City', ibge_data)

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)

def test_city_to_imediate_region():
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    ibge_data = {'municipios_regiao_imediata': {'saopaulo': 'São Paulo'}}

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_imediate_region(df, 'City', ibge_data)

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


def test_city_to_intermediarie_region():
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    ibge_data = {'municipios_regiao_intermediaria': {'saopaulo': 'São Paulo'}}

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_intermediarie_region(df, 'City', ibge_data)

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)

def test_city_to_state():
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    ibge_data = {'municipios_estado': {'saopaulo': 'São Paulo'}}

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_state(df, 'City', ibge_data)

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


def test_state_to_region():
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    ibge_data = {'regiao': {'saopaulo': 'São Paulo'}}

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = state_to_region(df, 'City', ibge_data)

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)

def test_cep_to_state():
    d = {
        'Customer': [1, 2, 3],
        'CEP' : ['03033-070', '03033070', '03033']
    } 

    df = pd.DataFrame(data=d)

    ibge_data = {'cep_estado':{pd.Interval(1000000, 19999999, closed='both'): 'São Paulo',pd.Interval(1000, 19999, closed='both'): 'São Paulo'}}

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo'], name='temp')

    result = cep_to_state(df, 'CEP', ibge_data)

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)



def test_cep_to_region():
    d = {
        'Customer': [1, 2, 3],
        'CEP' : ['03033-070', '03033070', '03033']
    } 

    df = pd.DataFrame(data=d)

    ibge_data = {'cep_estado':{pd.Interval(1000000, 19999999, closed='both'): 'São Paulo',pd.Interval(1000, 19999, closed='both'): 'São Paulo'},'regiao':{'São Paulo': 'Sudeste'}}

    expected = pd.Series(['Sudeste', 'Sudeste', 'Sudeste'], name='temp')

    result = cep_to_region(df, 'CEP', ibge_data)

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)
