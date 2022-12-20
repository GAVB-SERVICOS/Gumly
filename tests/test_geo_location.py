import mock
import numpy as np
import pandas as pd
from pandas.testing import assert_series_equal

ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_regiao': {'saopaulo': 'Sudeste'}}


@mock.patch("ibge.localidades.Estados")
@mock.patch("ibge.localidades.Municipios")
@mock.patch.dict("sys.modules", {"gumly.geo_location.ibge_data": ibge_data})
def test_fetch(e, m):
    from gumly.geo_location import fetch

    fetch()
    e.assert_called()
    m.assert_called()


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_city_to_region():
    from gumly.geo_location import city_to_region

    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }

    df = pd.DataFrame(data=d)

    d1 = {'Customer': [1, 2, 3], 'City': ['Bom jesus', 'Bom Jesus', 'Bom Jesus'], 'UF': ['RS', "PI", 'RN']}

    dfuf = pd.DataFrame(data=d1)

    expected = pd.Series(['Sudeste', 'Sudeste', 'Sudeste', np.nan], name='temp')

    result = city_to_region(df, 'City')

    expected1 = pd.Series(['Sul', 'Nordeste', 'Nordeste'], name='temp')

    result1 = city_to_region(dfuf, 'City', 'UF')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)

    assert_series_equal(result1, expected1, check_dtype=False, check_categorical=False)


ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_microrregiao': {'saopaulo': 'São Paulo'}}


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_city_to_microregion():
    from gumly.geo_location import city_to_microregion

    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }

    df = pd.DataFrame(data=d)

    d1 = {'Customer': [1, 2, 3], 'City': ['Bom jesus', 'Bom Jesus', 'Bom Jesus'], 'UF': ['RS', "PI", 'RN']}

    dfuf = pd.DataFrame(data=d1)

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_microregion(df, 'City')

    expected1 = pd.Series(['Vacaria', 'Alto Médio Gurguéia', 'Agreste Potiguar'], name='temp')

    result1 = city_to_microregion(dfuf, 'City', 'UF')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)

    assert_series_equal(result1, expected1, check_dtype=False, check_categorical=False)


ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_mesorregiao': {'saopaulo': 'São Paulo'}}


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_city_to_mesoregion():
    from gumly.geo_location import city_to_mesoregion

    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }

    df = pd.DataFrame(data=d)

    d1 = {'Customer': [1, 2, 3], 'City': ['Bom jesus', 'Bom Jesus', 'Bom Jesus'], 'UF': ['RS', "PI", 'RN']}

    dfuf = pd.DataFrame(data=d1)

    expected = pd.Series(
        ['Metropolitana de São Paulo', 'Metropolitana de São Paulo', 'Metropolitana de São Paulo', np.nan], name='temp'
    )

    result = city_to_mesoregion(df, 'City')

    expected1 = pd.Series(['Nordeste Rio-grandense', 'Sudoeste Piauiense', 'Agreste Potiguar'], name='temp')

    result1 = city_to_mesoregion(dfuf, 'City', 'UF')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)

    assert_series_equal(result1, expected1, check_dtype=False, check_categorical=False)


ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_regiao_imediata': {'saopaulo': 'São Paulo'}}


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_city_to_immediate_region():
    from gumly.geo_location import city_to_immediate_region

    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }

    df = pd.DataFrame(data=d)

    d1 = {'Customer': [1, 2, 3], 'City': ['Bom jesus', 'Bom Jesus', 'Bom Jesus'], 'UF': ['RS', "PI", 'RN']}

    dfuf = pd.DataFrame(data=d1)

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_immediate_region(df, 'City')

    expected1 = pd.Series(['Vacaria', 'Bom Jesus', 'Natal'], name='temp')

    result1 = city_to_immediate_region(dfuf, 'City', 'UF')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)

    assert_series_equal(result1, expected1, check_dtype=False, check_categorical=False)


ibge_data = mock.Mock()
ibge_data.return_value = {'municipios_regiao_intermediaria': {'saopaulo': 'São Paulo'}}


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_city_to_intermediary_region():
    from gumly.geo_location import city_to_intermediary_region

    d = {
        'Customer': [1, 2, 3, 4],
        'City': ['São Paulo', 'Sao Paulo', 'sao paulo', 'São Pauol'],
    }

    df = pd.DataFrame(data=d)

    d1 = {'Customer': [1, 2, 3], 'City': ['Bom jesus', 'Bom Jesus', 'Bom Jesus'], 'UF': ['RS', "PI", 'RN']}

    dfuf = pd.DataFrame(data=d1)

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo', np.nan], name='temp')

    result = city_to_intermediary_region(df, 'City')

    expected1 = pd.Series(['Caxias do Sul', 'Corrente - Bom Jesus', 'Natal'], name='temp')

    result1 = city_to_intermediary_region(dfuf, 'City', 'UF')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)
    assert_series_equal(result1, expected1, check_dtype=False, check_categorical=False)


ibge_data = mock.Mock()
ibge_data.return_value = {'regiao': {'saopaulo': 'São Paulo'}}


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
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
ibge_data.return_value = {
    'cep_estado': {
        pd.Interval(1000000, 19999999, closed='both'): 'São Paulo',
        pd.Interval(1000, 19999, closed='both'): 'São Paulo',
    }
}


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_cep_to_state():
    from gumly.geo_location import cep_to_state

    d = {'Customer': [1, 2, 3], 'CEP': ['03033-070', '03033070', '03033']}

    df = pd.DataFrame(data=d)

    expected = pd.Series(['São Paulo', 'São Paulo', 'São Paulo'], name='temp')

    result = cep_to_state(df, 'CEP')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


ibge_data = mock.Mock()
ibge_data.return_value = {
    'cep_estado': {
        pd.Interval(1000000, 19999999, closed='both'): 'São Paulo',
        pd.Interval(1000, 19999, closed='both'): 'São Paulo',
    },
    'regiao': {'São Paulo': 'Sudeste'},
}


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_cep_to_region():
    from gumly.geo_location import cep_to_region

    d = {'Customer': [1, 2, 3], 'CEP': ['03033-070', '03033070', '03033']}

    df = pd.DataFrame(data=d)

    expected = pd.Series(['Sudeste', 'Sudeste', 'Sudeste'], name='temp')

    result = cep_to_region(df, 'CEP')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_ibge_city():
    from gumly.geo_location import ibge_city

    d = {
        'Customer': [1, 2],
        'ID': ['5300108', '30'],
    }

    df = pd.DataFrame(data=d)

    expected = pd.Series(['Brasília', np.nan], name='temp')

    result = ibge_city(df, 'ID')

    np.array_equal(result.values, expected.values)


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_city_ibge():
    from gumly.geo_location import city_ibge

    d = {'Customer': [1, 2, 3], 'City': ['Bom jesus', 'Bom Jesus', 'Bom Jesus'], 'UF': ['RS', "PI", 'RN']}

    dfuf = pd.DataFrame(data=d)

    expected = pd.Series(['4302303', '2201903', '2401701'], name='temp')

    result = city_ibge(dfuf, 'City', 'UF')

    np.array_equal(result.values, expected.values)


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_state_uf():
    from gumly.geo_location import state_to_uf

    d = {'Customer': [1, 2, 3], 'state': ['Rio Grande do Sul', 'sao paulo', 'paraná']}

    dfs = pd.DataFrame(data=d)

    expected = pd.Series(['RS', 'SP', 'PR'], name='temp')

    result = state_to_uf(dfs, 'state')

    assert_series_equal(result, expected, check_dtype=False, check_categorical=False)


@mock.patch.dict(
    "sys.modules",
    {
        "gumly.geo_location.ibge_data": ibge_data,
    },
)
def test_uf_state():
    from gumly.geo_location import uf_to_state

    d = {'Customer': [1, 2, 3], 'state': ['rS', 'sP', 'Pr']}

    dfs = pd.DataFrame(data=d)

    expected = pd.Series(['Rio Grande do Sul', 'São Paulo', 'Paraná'], name='temp')

    result = uf_to_state(dfs, 'state')

    np.array_equal(result.values, expected.values)
