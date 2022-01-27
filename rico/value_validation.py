import pandas as pd


def check_number(x, lower=None, upper=None):
    """
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
    :param x: Value to be checked
    :type x: number
    :param lower: minimum value accepted
    :type lower: number
    :param upper: maximum value accepted
    :type upper: number
    :param varname: auxiliary variable for checking
    :type varname : str
    :raise AssertionError: expected value for varname

    """
    varname = varname or "x"
    assert check_number(
        x=x, lower=lower, upper=upper
    ), f"Check number of: {varname} ({type(x)})={x}, expected {varname} between {lower} and {upper}"


def check_dtypes(df: pd.DataFrame, types: list):
    """
    Module for verification of dataframe columns dtypes.

    :param df: DataFrame pandas
    :type: DataFrame
    :param check_types: check_types to check if exists in df
    :type: list of str
    :raise ValueError : The input columns must be different from [types]
    """

    if (df.dtypes.any() == i for i in types) == True:
        raise ValueError("The input columns must be different from %s", types)
