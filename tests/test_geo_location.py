
import mock
import pandas as pd
from pandas.testing import assert_series_equal
import numpy as np


ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_regiao': {'saopaulo': 'Sudeste'}}

@mock.patch.dict(
    "sys.modules", {"gumly.geo_location.ibge_data": ibge_data, }
)
def test_city_to_region():
    from gumly.geo_location import city_to_region
    
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    expected = pd.Series(['Sudeste', 'Sudeste', 'Sudeste', np.nan], name='temp')

    result = city_to_region(df, 'City')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_microrregiao': {'saopaulo': 'São Paulo'}}

@mock.patch.dict(
    "sys.modules", {"gumly.geo_location.ibge_data": ibge_data, }
)
def test_city_to_microregion():
    from gumly.geo_location import city_to_microregion
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_microregion(df, 'City')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)



ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_mesorregiao': {'saopaulo': 'São Paulo'}}

@mock.patch.dict(
    "sys.modules", {"gumly.geo_location.ibge_data": ibge_data, }
)
def test_city_to_mesoregion():
    from gumly.geo_location import city_to_mesoregion
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d) 

    expected = pd.Series(['Metropolitana de São Paulo', 'Metropolitana de São Paulo', 'Metropolitana de São Paulo', np.nan], name='temp')

    result = city_to_mesoregion(df, 'City')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_regiao_imediata': {'saopaulo': 'São Paulo'}}

@mock.patch.dict(
    "sys.modules", {"gumly.geo_location.ibge_data": ibge_data, }
)
def test_city_to_imediate_region():
    from gumly.geo_location import city_to_imediate_region
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_imediate_region(df, 'City')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)




ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_regiao_intermediaria': {'saopaulo': 'São Paulo'}}

@mock.patch.dict(
    "sys.modules", {"gumly.geo_location.ibge_data": ibge_data, }
)
def test_city_to_intermediarie_region():
    from gumly.geo_location import city_to_intermediary_region
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_intermediary_region(df, 'City')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)




ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_estado': {'saopaulo': 'São Paulo'}}

@mock.patch.dict(
    "sys.modules", {"gumly.geo_location.ibge_data": ibge_data, }
)
def test_city_to_state():
    from gumly.geo_location import city_to_state
    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_state(df, 'City')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)



ibge_data = mock.Mock()
ibge_data.return_value = {'regiao': {'saopaulo': 'São Paulo'}}

@mock.patch.dict(
    "sys.modules", {"gumly.geo_location.ibge_data": ibge_data, }
)
def test_state_to_region():
    from gumly.geo_location import state_to_region
    d = {
        'Customer': [1, 2, 3, 4],
        'State': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }  

    df = pd.DataFrame(data=d)

    expected = pd.Series(['Sudeste', 'Sudeste', 'Sudeste', np.nan], name='temp')

    result = state_to_region(df, 'State')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)



ibge_data = mock.Mock()
ibge_data.return_value = {'cep_estado':{pd.Interval(1000000, 19999999, closed='both'): 'São Paulo',pd.Interval(1000, 19999, closed='both'): 'São Paulo'}}

@mock.patch.dict(
    "sys.modules", {"gumly.geo_location.ibge_data": ibge_data, }
)
def test_cep_to_state():
    from gumly.geo_location import cep_to_state
    d = {
        'Customer': [1, 2, 3],
        'CEP' : ['03033-070', '03033070', '03033']
    } 

    df = pd.DataFrame(data=d)

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo'], name='temp')

    result = cep_to_state(df, 'CEP')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


ibge_data = mock.Mock()
ibge_data.return_value = {'cep_estado':{pd.Interval(1000000, 19999999, closed='both'): 'São Paulo',pd.Interval(1000, 19999, closed='both'): 'São Paulo'},'regiao':{'São Paulo': 'Sudeste'}}

@mock.patch.dict(
    "sys.modules", {"gumly.geo_location.ibge_data": ibge_data, }
)
def test_cep_to_region():
    from gumly.geo_location import cep_to_region
    d = {
        'Customer': [1, 2, 3],
        'CEP' : ['03033-070', '03033070', '03033']
    } 

    df = pd.DataFrame(data=d)

    expected = pd.Series(['Sudeste', 'Sudeste', 'Sudeste'], name='temp')

    result = cep_to_region(df, 'CEP')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


@mock.patch.dict(
    "sys.modules", {"gumly.geo_location.ibge_data": ibge_data, }
)
def test_id_to_city():
    from gumly.geo_location import ibge_city
    d = {
        'Customer': [1, 2],
        'ID': ['5300108','30'],
    }  

    df = pd.DataFrame(data=d)

    expected = pd.Series(['Brasília', np.nan], name='temp')

    result = ibge_city(df, 'ID')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)

