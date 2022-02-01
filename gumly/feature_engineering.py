from typing import Any, List, Set

import pandas as pd
import statsmodels.api as sm
from lightgbm import LGBMClassifier
from sklearn.feature_selection import (
    RFE,
    SelectFromModel,
    SelectKBest,
    chi2,
    f_regression,
    mutual_info_regression,
)
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler

from gumly.value_validation import assert_check_dtypes, assert_check_number


def split_features_and_target(df: pd.DataFrame, target: str):
    """
    Separates the features and the target columns into two new dataframes, one containing each.

    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :return: x, y for modeling process
    :rtype: DataFrame | Series
    """

    x = df.drop(columns=[str(target)], axis=1)
    y = df[str(target)]

    return x, y


def feature_selection_filter(df: pd.DataFrame, target: str, num_feats: int):
    """
    Feature selection using filter technique and chi2 values, this function returns
    the main important features based on chi2 test as a list.

    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param num_feats: The number of features that is wanted to remain after the process
    :type: int
    :return: features selected by the technique
    :rtype: list
    """

    assert_check_dtypes(df, ['str'])

    x, y = split_features_and_target(df, target)

    x_norm = MinMaxScaler().fit_transform(x)
    chi_selector = SelectKBest(chi2, k=num_feats)
    chi_selector.fit(x_norm, y)
    chi_support = chi_selector.get_support()
    chi_feature = x.loc[:, chi_support].columns.tolist()

    return chi_feature


def feature_selection_wrapper(df: pd.DataFrame, target: str, num_feats: int, step: int = 10):
    """
    Feature selection using wrapper technique and LogisticRegression, this function returns
    the main important features based on betas from LogisticRegression algorithm as a list.

    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param num_feats: The number of features that is wanted to remain after the process
    :type: int
    :param step: The number steps
    :type: int, default = 10
    :return: features selected by the technique
    :rtype: list
    """

    assert_check_dtypes(df, ['str'])

    x, y = split_features_and_target(df, target)

    rfe_selector = RFE(
        estimator=LogisticRegression(max_iter=200),
        n_features_to_select=num_feats,
        step=step,
    )
    rfe_selector.fit(x, y)
    rfe_support = rfe_selector.get_support()
    rfe_feature = x.loc[:, rfe_support].columns.tolist()

    return rfe_feature


def feature_selection_embedded(df: pd.DataFrame, target: str, num_feats: int, n_estimators: int):
    """
    Feature selection using embedded technique and LightGBMClassifier, this function returns
    the main important features based on feature importance as a list.

    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param num_feats: The number of features that is wanted to remain after the process as max value
    :type: int
    :param n_estimators: The number of estimators for the training phase
    :type: int
    :return: features selected by the technique
    :rtype: list
    """

    assert_check_dtypes(df, ['str'])

    x, y = split_features_and_target(df, target)

    lgbc = LGBMClassifier(n_estimators=n_estimators)
    embeded_lgb_selector = SelectFromModel(lgbc, max_features=num_feats)
    embeded_lgb_selector.fit(x, y)
    embeded_lgb_support = embeded_lgb_selector.get_support()
    embeded_lgb_feature = x.loc[:, embeded_lgb_support].columns.tolist()

    return embeded_lgb_feature


def feature_selection_stepwise(
    df,
    target: str,
    threshold_in: float = 0.01,
    threshold_out: float = 0.05,
    verbose: bool = False,
):
    """
    Perform a forward-backward feature selection based on p-value from statsmodels.api.OLS.

    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param threshold_in: include a feature if its p-value < threshold_in
    :type: float, default = 0.01
    :param threshold_out: exclude a feature if its p-value > threshold_out
    :type: float, default = 0.05
    :param verbose: whether to print the sequence of inclusions and exclusions
    :type: bool, default = False
    :return: features selected by the technique
    :rtype: list
    """

    assert_check_dtypes(df, ['str'])

    x, y = split_features_and_target(df, target)

    included: List[pd.Series] = []
    while True:
        changed = False
        excluded = list(set(x.columns) - set(included))
        new_pval = pd.Series(index=excluded)
        for new_column in excluded:
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(x[included + [new_column]]))).fit()
            new_pval[new_column] = model.pvalues[new_column]
        best_pval = new_pval.min()
        if best_pval < threshold_in:
            best_feature = new_pval.idxmin()
            included.append(best_feature)
            changed = True
            if verbose:
                print("Add  {:30} with p-value {:.6}".format(best_feature, best_pval))

        model = sm.OLS(y, sm.add_constant(pd.DataFrame(x[included]))).fit()
        pvalues = model.pvalues.iloc[1:]
        worst_pval = pvalues.max()
        if worst_pval > threshold_out:
            changed = True
            worst_feature = pvalues.idxmax()
            included.remove(worst_feature)
            if verbose:
                print("Drop {:30} with p-value {:.6}".format(worst_feature, worst_pval))
        if not changed:
            break

    return included


def feature_selection_f_regression(df: pd.DataFrame, target: str, num_feats: int):
    """
    Perform a f_regression feature selection based on p-value, returns
    the main important features based on p-value as a list.

    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param num_feats: The number of features that is wanted to remain after the process
    :type: int
    :return: features selected by the technique
    :rtype: list
    """

    assert_check_dtypes(df, ['str'])

    x, y = split_features_and_target(df, target)

    f_reg = SelectKBest(f_regression, k=num_feats)
    f_reg.fit(x, y)
    f_support = f_reg.get_support()
    f_feature = x.loc[:, f_support].columns.tolist()

    return f_feature


def feature_selection_mutual_information(df: pd.DataFrame, target: str, num_feats: int):
    """
    Perform a mutual_info_regression feature selection, the return of the function are
    main important features based on mutual information score as a list.

    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param num_feats: The number of features that is wanted to remain after the process
    :type: int
    :return: features selected by the technique
    :rtype: list
    """

    assert_check_dtypes(df, ['str'])

    x, y = split_features_and_target(df, target)

    random_state = 42

    m_info = SelectKBest(score_func=lambda x, y: mutual_info_regression(x, y, random_state=random_state), k=num_feats)
    m_info.fit(x, y)
    mi_support = m_info.get_support()
    mi_feature = x.loc[:, mi_support].columns.tolist()

    return mi_feature


def ordering_filter(
    data,
    variables,
    lower_percentile: float = 0.0,
    upper_percentile: float = 0.0,
):

    """
    Analyzes the records of all given variables and returns their indexes if their values are among
    the values within the fraction (lower_percentile) of the smallest values or if their values
    are among the values within the fraction (upper_percentile) of the biggest values.

    :param data : data frame
    :type: DataFrame
    :param variables: variables to be treated for the method
    :type: str or list
    :param lower_percentile: minimum percentile threshold
    :type: float, default = 0.0
    :param upper_percentile: maximum percentile threshold
    :type: float, default = 0.0
    :return: list of outliers indices
    :rtype: list

    """

    assert_check_number(lower_percentile, 0, 1.0, "lower_percentile")
    assert_check_number(upper_percentile, 0, 1.0, "upper_percentile")

    if type(variables) == str:
        variables = variables.split()
    rows_to_drop: Set[Any] = set()
    quartil_lower = lower_percentile
    quartil_upper = 1.0 - upper_percentile
    data_len = len(data)
    index_lower = quartil_lower * data_len
    index_upper = quartil_upper * data_len
    for var in variables:
        new_data = data.copy().sort_values(by=var, ascending=False)
        new_data["__index__"] = list(range(1, data_len + 1))
        rows_to_drop = rows_to_drop.union(
            set(new_data[(new_data["__index__"] <= index_lower) | (new_data["__index__"] >= index_upper)].index)
        )
    return list(rows_to_drop)
