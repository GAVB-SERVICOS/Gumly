import pandas as pd

def variable_treat(
    data,
    variables,
    lower: bool = False,
    lower_percentile: float = None,
    upper: bool = False,
    upper_percentile: float = None,
):

    """
    Select the outliers list
    
    :param data : data frame
    :type: DataFrame 
    :param variables: variables to treat
    :type: str or list 
    :param lower: method to select lower values    
    :type: bool  
    :param lower_percentile: minimum percentile threshold 
    :type: float
    :param upper: method to select upper values   
    :type: bool  
    :param upper_percentile: maximum percentile threshold 
    :type: float
    :raise NotImplementedError: or lower or upper must be True  
    :return: list of outliers indices
    :rtype: list

    """

    if lower is False and upper is False:
        raise NotImplementedError(f" One of those paramns must be True")

    if type(variables) == str:
        variables = variables.split()
    rows_to_drop = set()

    if lower:
        lp = lower_percentile / 100
        for var in variables:
            new_data = data.copy().sort_values(by=var)
            new_data["New Column"] = range(1, 1 + new_data.shape[0])
            rows_to_drop = rows_to_drop.union(
                set(new_data[new_data["New Column"] < (lp * new_data.shape[0])].index)
            )

    if upper:
        up = upper_percentile / 100
        for var in variables:
            new_data = data.copy().sort_values(by=var)
            new_data["New Column"] = range(1, 1 + new_data.shape[0])
            rows_to_drop = rows_to_drop.union(
                set(new_data[new_data["New Column"] > (up * new_data.shape[0])].index)
            )

    rows_to_drop = list(rows_to_drop)

    return rows_to_drop


data = pd.read_csv('aluguel.csv', sep = ';')
variable_treat(data, 'Condominio', lower = True, lower_percentile=1.0, upper=True, upper_percentile=90.0)



