


def check_number(x, lower=None, upper=None, varname=None):
   
    if varname is None:
        varname = 'x'
   
    if x is not None:
        if not isinstance(x, float) and not isinstance(x, int):
            raise TypeError(f"The variable {varname} percentile must be a number")
        if (lower is not None and x < lower) or (upper is not None and x > upper):
            raise ValueError(f"The variable {varname} must be between {lower} and {upper}")