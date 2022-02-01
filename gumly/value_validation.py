import pandas as pd


def check_number(x, lower=None, upper=None):
    """
    This function returns True if the first argument is a number and it lies between the next two arguments.
    Othwerise, returns False.

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
    This function uses the above function and it will raise an exception if check_number returns False.

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
