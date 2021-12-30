import pandas as pd
from sklearn.feature_selection import (
    SelectKBest,
    chi2,
    RFE,
    SelectFromModel,
    f_regression,
    mutual_info_regression,
)
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
from lightgbm import LGBMClassifier
import statsmodels.api as sm
from mlutils.attribute_validation import check_number


def select_data(df: pd.DataFrame, target: str):
    """
    Select dataframe and the name of the target variable as input and return x,y.
    
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


def feature_selection_filter(df, target: str, num_feats: int):
    """
    Feature selection using filter technique and chi2 values.
    
    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param num_feats: The number of features that is wanted to remain after the process
    :type: int
    :return: features selected by the technique
    :rtype: list
    """
    x, y = select_data(df, target)

    x_norm = MinMaxScaler().fit_transform(x)
    chi_selector = SelectKBest(chi2, k=num_feats)
    chi_selector.fit(x_norm, y)
    chi_support = chi_selector.get_support()
    chi_feature = x.loc[:, chi_support].columns.tolist()

    return chi_feature


def feature_selection_wrapper(df, target: str, num_feats: int, step: int = 10):
    """
    Feature selection using wrapper technique and LogisticRegression.
    
    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param num_feats: The number of features that is wanted to remain after the process
    :type: int
    :param step: The number steps
    :type: int
    :return: features selected by the technique
    :rtype: list
    """
    x, y = select_data(df, target)

    rfe_selector = RFE(
        estimator=LogisticRegression(max_iter=200),
        n_features_to_select=num_feats,
        step=step,
    )
    rfe_selector.fit(x, y)
    rfe_support = rfe_selector.get_support()
    rfe_feature = x.loc[:, rfe_support].columns.tolist()

    return rfe_feature


def feature_selection_embedded(df, target: str, num_feats: int, n_estimators: int):
    """
    Feature selection using embedded technique and LightGBMClassifier.
    
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

    x, y = select_data(df, target)

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
    Perform a forward-backward feature selection based on p-value from statsmodels.api.OLS
    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param threshold_in: include a feature if its p-value < threshold_in
    :type: float
    :param threshold_out: exclude a feature if its p-value > threshold_out
    :type: float
    :param verbose: whether to print the sequence of inclusions and exclusions
    :type: bool
    :return: features selected by the technique
    :rtype: list
    """
    x, y = select_data(df, target)

    initial_list = []

    included = list(initial_list)
    while True:
        changed = False
        excluded = list(set(x.columns) - set(included))
        new_pval = pd.Series(index=excluded)
        for new_column in excluded:
            model = sm.OLS(
                y, sm.add_constant(pd.DataFrame(x[included + [new_column]]))
            ).fit()
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


def feature_selection_f_regression(df, target: str, num_feats: int):
    """ 
    Perform a f_regression feature selection based on p-value
    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param num_feats: The number of features that is wanted to remain after the process
    :type: int
    :return: features selected by the technique
    :rtype: list
    """

    x, y = select_data(df, target)

    f_reg = SelectKBest(f_regression, k=num_feats)
    f_reg.fit(x, y)
    f_support = f_reg.get_support()
    f_feature = x.loc[:, f_support].columns.tolist()

    return f_feature


def feature_selection_mutual_information(df, target: str, num_feats: int):
    """ 
    Perform a mutual_info_regression feature selection
    :param df: DataFrame pandas
    :type: DataFrame
    :param target: target variable
    :type: str
    :param num_feats: The number of features that is wanted to remain after the process
    :type: int
    :return: features selected by the technique
    :rtype: list
    """
    x, y = select_data(df, target)
    random_state = 42

    m_info = SelectKBest(
        score_func=lambda x, y: mutual_info_regression(x, y, random_state=random_state),
        k=num_feats,
    )
    m_info.fit(x, y)
    mi_support = m_info.get_support()
    mi_feature = x.loc[:, mi_support].columns.tolist()

    return mi_feature




def ordering_filter(
    data,
    variables,
    lower_percentile: float = None,
    upper_percentile: float = None,
):

    """
    Returns the indexes of the records that have its values among the
    <lower_percentile>% smaller and/or have its values among the
    <upper_percentile>% bigger.
   
    :param data : data frame
    :type: DataFrame
    :param variables: variables to be treated for the method
    :type: str or list
    :param lower_percentile: minimum percentile threshold
    :type: float
    :param upper_percentile: maximum percentile threshold
    :type: float
    :raise NotImplementedError: or lower or upper must be True  
    :return: list of outliers indices
    :rtype: list
    """

    check_number(lower_percentile, 0, 100, 'lower_percentile')
    check_number(upper_percentile, 0, 100, 'upper_percentile')
   
    if type(variables) == str:
        variables = variables.split()
    rows_to_drop = set()

    if lower_percentile is not None:
        lp = lower_percentile / 100
        for var in variables:
            new_data = data.copy().sort_values(by=var)
            new_data["New Column"] = range(1, 1 + new_data.shape[0])
            rows_to_drop = rows_to_drop.union(
                set(new_data[new_data["New Column"] <= (lp * new_data.shape[0])].index)
            )

    if upper_percentile is not None:
        up = upper_percentile / 100
        for var in variables:
            new_data = data.copy().sort_values(by=var, ascending=False)
            new_data["New Column"] = range(1, 1 + new_data.shape[0])
            rows_to_drop = rows_to_drop.union(
                set(new_data[new_data["New Column"] <= (up * new_data.shape[0])].index)
            )

    rows_to_drop = list(rows_to_drop)

    return rows_to_drop