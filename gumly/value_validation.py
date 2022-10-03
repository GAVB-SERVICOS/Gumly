import sys

import pandas as pd


def check_number(x, lower=None, upper=None):
    """
    This function returns True if the first argument is a number and it lies between the next two arguments.
    Otherwise, returns False.

    :param x: Value to be checked
    :type x: number
    :param lower: minimum value accepted
    :type lower: number
    :param upper: maximum value accepted
    :type upper: number
    :return: if 'x' check pass
    :rtype: bool

    """

    if x is None:
        return False
    lower = lower if lower is not None else float("-inf")
    upper = upper if upper is not None else float("inf")
    is_number = isinstance(x, float) or isinstance(x, int)
    return is_number and (x >= lower and x <= upper)


def assert_check_number(x, lower=None, upper=None, varname=None):
    """
    This function uses the check_number function and it will raise an exception if it returns False.

    :param x: Value to be checked
    :type x: number
    :param lower: minimum value accepted
    :type lower: number
    :param upper: maximum value accepted
    :type upper: number
    :param varname: The name of the variable shown in the error message
    :type varname : str
    :raise AssertionError: 'x' is not a number or is not between 'lower' and 'upper'

    """
    varname = varname or "x"
    assert check_number(
        x=x, lower=lower, upper=upper
    ), f"Check number of: {varname} ({type(x)})={x}, expected {varname} between {lower} and {upper}"


def check_int(x: int, lower: int = None, upper: int = None) -> bool:
    """
    This function returns True if the first argument is an integer and it
    lies between the next two arguments. Otherwise, returns False.

    :param x: Value to be checked
    :type x: Integer
    :param lower: minimum value accepted
    :type lower: Integer
    :param upper: maximum value accepted
    :type upper: Integer

    :return: True if 'x' is an integer and is between 'lower' and 'upper'.
        False, otherwise
    :rtype: bool

    """
    if x is None:
        return False
    # Take the max and minimum integer values
    max_size = sys.maxsize
    min_size = -sys.maxsize - 1

    lower = lower if lower is not None else min_size
    upper = upper if upper is not None else max_size
    is_int = isinstance(x, int)
    return is_int and (lower <= x <= upper)


def assert_check_int(x: int, lower: int = None, upper: int = None, varname: str = None):
    """
    This function uses the check_int function and it will raise an exception if it returns False.

    :param x: Value to be checked
    :type x: Integer
    :param lower: minimum value accepted
    :type lower: Integer
    :param upper: maximum value accepted
    :type upper: Integer
    :param varname: The name of the variable shown in the error message
    :type varname : str

    :raise AssertionError: 'x' is not an integer or is not between 'lower' and 'upper'

    """
    varname = varname or "x"
    assert check_int(
        x=x, lower=lower, upper=upper
    ), f"Check integer of: {varname} ({type(x)})={x}, expected {varname} between {lower} and {upper}"


def check_list(target: list, n_elements: int = None, type_of_elements=None) -> bool:
    """
    Checks whether the given value is a list. Optionally, verifies if it has
    some specific number of elements and/or if all elements are instances of a
    given type/class. It returns True if all checks pass and False otherwise.

    :param target: The value for inspection
    :type target: List
    :param n_elements: The number of elements the list should contain
    :type n_elements: Integer
    :param type_of_elements: The class/type which all elements of the
        list should be instances of
    :type type_of_elements: Any class or type object

    :return: True if all checks pass, False otherwise
    :rtype: Bool
    """

    # initialize the checks values
    elements_ok = True
    types_ok = True
    is_list = False

    # check if l is really a list, ...
    if isinstance(target, list):
        # if it is, lets try the other checks

        # if n_elements is valid, ...
        if n_elements is not None and isinstance(n_elements, int):
            # if l has a different number of elements, record it
            if len(target) != n_elements:
                elements_ok = False

        # if type_of_elements is valid, ...
        if type_of_elements is not None:
            # check every element in l
            for element in target:
                # if the element is not of the expected type, ...
                if not isinstance(element, type_of_elements):
                    # the list has failed the type of element test
                    types_ok = False
                    break

        # mark it as a list
        is_list = True

    # return the combined results of all checks
    return is_list and elements_ok and types_ok


def assert_check_list(target: list, n_elements: int = None, type_of_elements=None, varname: str = None):
    """
    This function uses the check_list function and it will raise an exception if it returns False.

    :param target: Value to be checked
    :type target: Integer
    :param n_elements: The number of elements the list should contain
    :type n_elements: Integer
    :param type_of_elements: The class/type which all elements of the
        list should be instances of
    :type type_of_elements: Any class or type object
    :param varname: The name of the variable shown in the error message
    :type varname : String

    :raise AssertionError: 'x' is not a list or if it doesnt have a specific
        number of elements or if one of its elements is not of a given type/class
    """
    varname = varname or "target"

    n = n_elements if n_elements is not None and type(n_elements) is int else 'any number of'
    t = type_of_elements if type_of_elements is not None else 'anything'

    assert check_list(target=target, n_elements=n_elements, type_of_elements=type_of_elements), (
        f"Check list of: {varname} ({type(target)})={target}, expected {varname} to be a list with "
        f"{n} elements and its elements to be {t}"
    )


def check_dtypes(df: pd.DataFrame, types: list):
    """
    Module for verification of the list of types.

    :param df: DataFrame pandas
    :type: DataFrame
    :param types: list of desired dtypes to check in df
    :type: list of str
    :raise ValueError : The input is empty
    :return: column from df
    :rtype: str
    """

    if len(types) == 0:
        raise ValueError("The input is empty")

    for k, v in df.dtypes.to_dict().items():
        if v in types:
            return k
    return None


def assert_check_dtypes(df: pd.DataFrame, types: list):
    """
    Module for verification of dataframe columns dtypes.

    :param df: DataFrame pandas
    :type: DataFrame
    :param types: list of desired dtypes to check in df
    :type: list of str
    :raise AssertError : type of column {k} is not permitted
    """

    k = check_dtypes(df, types)

    assert k is None, f"type of column {k} is not permitted"
