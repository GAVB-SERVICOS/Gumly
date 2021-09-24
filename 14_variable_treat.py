
import numpy as np


def variable_treat(data,
                   variables,
                   lower = False,
                   lower_percentile = 1,
                   lower_threshold = 0,
                   upper = False,
                   upper_percentile = 99,
                   upper_threshold = 0):
    
    if type(variables) == str:
        variables = variables.split()
    rows_to_drop = set()
    
    if lower:
        for var in variables:
            p = np.percentile(data[var], lower_percentile) - lower_threshold
            for row in data.index:
                if data[var][row] < p:
                    rows_to_drop.add(row)
            print(len(rows_to_drop))
    
    if upper:
        for var in variables:
            p = np.percentile(data[var], upper_percentile) + upper_threshold
            for row in data.index:
                if data[var][row] > p:
                    rows_to_drop.add(row)
            print(len(rows_to_drop))
    
    return rows_to_drop