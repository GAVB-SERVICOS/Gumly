import pandas as pd
import pytest

from gumly.value_validation import (
    assert_check_dtypes,
    assert_check_number,
    check_dtypes,
    check_number,
)


def test_argument_validation_check_number():

    assert True == check_number(1, 0, 100)
    assert False == check_number(-1, 0, 100)
    assert True == check_number(0.25, 0, 1)
    assert False == check_number("string")
    assert False == check_number(list(), 0, 1)
    assert False == check_number(dict())


def test_argument_validation_check():

    lower_percentil = 1

    assert_check_number(lower_percentil, 0, 1.0, "lower_percentil")


def test_argument_validation_error():
    with pytest.raises(AssertionError):

        lower_percentil = -1

        assert_check_number(lower_percentil, 0, 1.0, "lower_percentil")


def test_check_dtypes():

    x = pd.DataFrame({'a': [1, 2, 3], 'b': ['1', '2', '3']})

    with pytest.raises(ValueError):
        check_dtypes(x, [])

    assert None == check_dtypes(x, ['float64'])


def test_assert_check_dtypes_error():

    x = pd.DataFrame({'a': [1, 2, 3], 'b': ['1', '2', '3']})
    y = pd.DataFrame({'a': [1, 2, 3], 'b': [1.0, 1.2, 3.0]})

    with pytest.raises(AssertionError):

        y = pd.DataFrame({'a': [1, 2, 3], 'b': [1.0, 1.2, 3.0]})

        assert_check_dtypes(y, ['float64'])

    assert None == assert_check_dtypes(x, ['float64'])
