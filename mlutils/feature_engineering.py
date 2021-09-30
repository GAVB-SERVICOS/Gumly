# ref: https://github.com/gavbdheiver/predictive-maintenance-accelerator-/blob/main/predictive-maintenance-accelerator/Feature%20selection/Feat_Selection_Com_Stepwise/RUL_OPTUNA_DB4_Stepwise_Regression.ipynb

import pandas as pd
import numpy as np

from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
from sklearn.preprocessing import MinMaxScaler

from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

from sklearn.feature_selection import SelectFromModel
from lightgbm import LGBMClassifier



def select_data(df, target):
    x = df.drop(columns=['{}'.format(target)], axis=1)
    y = df['{}'.format(target)]

    return x, y


def feature_selection_filter(df, target, num_feats):
    x, y = select_data(df, target)
    
    x_norm = MinMaxScaler().fit_transform(x)
    chi_selector = SelectKBest(chi2, k=num_feats)
    chi_selector.fit(x_norm, y)
    chi_support = chi_selector.get_support()
    chi_feature = x.loc[:,chi_support].columns.tolist()
    
    return chi_feature



def feature_selection_wrapper(df, target, num_feats):
    x, y = select_data(df, target)

    rfe_selector = RFE(estimator=LogisticRegression(), n_features_to_select=num_feats, step=10)
    rfe_selector.fit(X_norm, y)
    rfe_support = rfe_selector.get_support()
    rfe_feature = X.loc[:,rfe_support].columns.tolist()
    
    return rfe_feature


def feature_selection_embedded(df, target):
    x, y = select_data(df, target)
    
    lgbc = LGBMClassifier(n_estimators=500) 
    embeded_lgb_selector = SelectFromModel(lgbc, max_features=num_feats)
    embeded_lgb_selector.fit(X, y)

    embeded_lgb_support = embeded_lgb_selector.get_support()
    embeded_lgb_feature = X.loc[:,embeded_lgb_support].columns.tolist()
    
    return embeded_lgb_feature


def stepwise_selection(X, y, 
                           initial_list=[], 
                           threshold_in=0.01, 
                           threshold_out = 0.05, 
                           verbose=True):
        """ Perform a forward-backward feature selection 
        based on p-value from statsmodels.api.OLS
        Arguments:
            X - pandas.DataFrame with candidate features
            y - list-like with the target
            initial_list - list of features to start with (column names of X)
            threshold_in - include a feature if its p-value < threshold_in
            threshold_out - exclude a feature if its p-value > threshold_out
            verbose - whether to print the sequence of inclusions and exclusions
        Returns: list of selected features 
        Always set threshold_in < threshold_out to avoid infinite looping.
        See https://en.wikipedia.org/wiki/Stepwise_regression for the details
        """
        included = list(initial_list)
        while True:
            changed=False
            # forward step
            excluded = list(set(X.columns)-set(included))
            new_pval = pd.Series(index=excluded)
            for new_column in excluded:
                model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included+[new_column]]))).fit()
                new_pval[new_column] = model.pvalues[new_column]
            best_pval = new_pval.min()
            if best_pval < threshold_in:
                best_feature = new_pval.idxmin()
                included.append(best_feature)
                changed=True
                if verbose:
                    print('Add  {:30} with p-value {:.6}'.format(best_feature, best_pval))

            # backward step
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included]))).fit()
            # use all coefs except intercept
            pvalues = model.pvalues.iloc[1:]
            worst_pval = pvalues.max() # null if pvalues is empty
            if worst_pval > threshold_out:
                changed=True
                worst_feature = pvalues.idxmax()
                included.remove(worst_feature)
                if verbose:
                    print('Drop {:30} with p-value {:.6}'.format(worst_feature, worst_pval))
            if not changed:
                break
        return included

    result = stepwise_selection(X, y)



