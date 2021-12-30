def check_number(x, lower=None, upper=None, varname=None):
    """
    Implements a method to check if the attribute passed is a number and if it's 
    not out of the range.
    
    :param x: the varname used for the check, it's the lower or upper attribute
    from another method
    :type: str
    :param lower: minimum percentile threshold
    :type: float, default = None 
    :param upper: maximum percentile threshold
    :type: float, default = None
    :param varname: Auxiliary variable for the checking
    :type: str, default = None
    :raise TypeError: The variable {varname} percentile must be a number.
    :raise ValueError : The variable {varname} must be between {lower} and {upper}

    """

    if varname is None:
        varname = "x"

    if x is not None:
        if not isinstance(x, float) and not isinstance(x, int):
            raise TypeError(f"The variable {varname} percentile must be a number")
        if (lower is not None and x < lower) or (upper is not None and x > upper):
            raise ValueError(
                f"The variable {varname} must be between {lower} and {upper}"
            )
