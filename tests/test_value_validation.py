import pandas as pd
import pytest

from gumly.value_validation import (
    assert_check_dtypes,
    assert_check_number,
    assert_check_int,
    assert_check_list,
    check_dtypes,
    check_number,
    check_int,
    check_list,
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


def test_check_int():

    assert True == check_int(10)  # no limits
    assert True == check_int(10, 0, 10)  # with both limits
    assert True == check_int(10, upper=10)  # with only upper limit
    assert True == check_int(10, lower=1)  # with only lower limit
    # with negative values
    assert True == check_int(-10)
    assert True == check_int(-10, -10, 0)
    assert True == check_int(-10, upper=0)
    assert True == check_int(-10, lower=-10)
    # should fail
    assert False == check_int(dict())  # with dicts
    assert False == check_int(5.6)  # with floats
    assert False == check_int([1, 2, 3, 4, 5], 0, 6)  # with lists
    assert False == check_int(None)  # with None
    assert False == check_int("4", 2, 5)  # with strings
    assert False == check_int(6, 0, 4)  # outside the boundaries (upper)
    assert False == check_int(6, 8, 10)  # outside the boundaries (lower)


def test_assert_check_int():

    # should be ok
    assert_check_int(10)  # no limits
    assert_check_int(10, 0, 10)  # with both limits
    assert_check_int(10, upper=10)  # with only upper limit
    assert_check_int(10, lower=1)  # with only lower limit
    # with negative values
    assert_check_int(-10)
    assert_check_int(-10, -10, 0)
    assert_check_int(-10, upper=0)
    assert_check_int(-10, lower=-10)
    # should fail
    with pytest.raises(AssertionError):
        assert_check_int(dict())  # with dicts
    with pytest.raises(AssertionError):
        assert_check_int(5.6)  # with floats
    with pytest.raises(AssertionError):
        assert_check_int([1, 2, 3, 4, 5], 0, 6)  # with lists
    with pytest.raises(AssertionError):
        assert_check_int(None)  # with None
    with pytest.raises(AssertionError):
        assert_check_int("4", 2, 5)  # with strings
    with pytest.raises(AssertionError):
        assert_check_int(6, 0, 4)  # outside the boundaries (upper)
    with pytest.raises(AssertionError):
        assert_check_int(6, 8, 10)  # outside the boundaries (lower)


def test_check_list():
    class A:
        def __init__(self, x):
            self.x = x

    assert True == check_list([1, 2, 3])  # simple list
    assert True == check_list(list())  # empty list
    assert True == check_list([1, 2, 3], n_elements=3, type_of_elements=int)  # with both checks
    assert True == check_list([1, 2, 3], n_elements=3)  # with number of elements
    assert True == check_list([1, 2, 3], type_of_elements=int)  # with types
    assert True == check_list([A(1), A(2), A(3)], type_of_elements=A)  # with custom classes
    assert True == check_list([1, 2, 3], type_of_elements=None)  # with no defined type
    assert True == check_list([1, 2, 3], n_elements="a")  # with invalid number of elements
    # should fail
    assert False == check_list(dict())  # with dicts
    assert False == check_list(2.5)  # with a number
    assert False == check_list("[1, 2]")  # with a string
    assert False == check_list(A(1))  # with a custom class
    assert False == check_list([1, 2, 3], n_elements=2)  # different number of elements
    assert False == check_list([1, "2", 3], type_of_elements=int)  # different type of element
    assert False == check_list([A(1), 2, A(3)], type_of_elements=A)  # different type with custom class


def test_assert_check_list():
    class A:
        def __init__(self, x):
            self.x = x

    assert_check_list([1, 2, 3])  # simple list
    assert_check_list(list())  # empty list
    assert_check_list([1, 2, 3], n_elements=3, type_of_elements=int)  # with both checks
    assert_check_list([1, 2, 3], n_elements=3)  # with number of elements
    assert_check_list([1, 2, 3], type_of_elements=int)  # with types
    assert_check_list([A(1), A(2), A(3)], type_of_elements=A)  # with custom classes
    assert_check_list([1, 2, 3], type_of_elements=None)  # with no defined type
    assert_check_list([1, 2, 3], n_elements="a")  # with invalid number of elements
    # should fail
    with pytest.raises(AssertionError):
        assert_check_list(dict())  # with dicts
    with pytest.raises(AssertionError):
        assert_check_list(2.5)  # with a number
    with pytest.raises(AssertionError):
        assert_check_list("[1, 2]")  # with a string
    with pytest.raises(AssertionError):
        assert_check_list(A(1))  # with a custom class
    with pytest.raises(AssertionError):
        assert_check_list([1, 2, 3], n_elements=2)  # different number of elements
    with pytest.raises(AssertionError):
        assert_check_list([1, "2", 3], type_of_elements=int)  # different type of element
    with pytest.raises(AssertionError):
        assert_check_list([A(1), 2, A(3)], type_of_elements=A)  # different type with custom class