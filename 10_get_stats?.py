## creating function to get model statistics
import numpy as np
import statsmodels.api as sm


def get_stats(): #Foi colocada como um talvez verificar com Paulo
    x = train_data[x_columns]
    results = sm.OLS(y, x).fit()
    print(results.summary())
get_stats()