import pandas as pd
import statsmodels.formula.api as smf


def stepwise_selection(data_dumm,
                       default,
                       initial_list = [], 
                       threshold_in = 0.01, 
                       threshold_out = 0.05,
                       inversion = True,
                       verbose = True):
    
    new_data = data_dumm.copy()
    target = default.copy()
    included = list(initial_list)
    
    while True:
        
        changed = False
        
        # forward step
        if verbose:
            print('>>>>>>forward step')
        
        excluded = list(set(new_data.columns) - set(included))
        forward_dict = {}
        
        for feature in excluded:
            
            formula = 'target ~ ' + ' + '.join([feature] + included)
            log_reg = smf.logit(formula, new_data).fit_regularized(disp = 0)
            forward_dict[feature] = log_reg.pvalues.loc[feature]
            
        forward_report = pd.Series(data = forward_dict.values(), index = forward_dict.keys())
        best_pvalue = forward_report.min()
        best_feature = forward_report.idxmin()

        if best_pvalue < threshold_in:
            included.append(best_feature)
            changed = True
            if verbose:
                print(f'ADD {best_feature}')
        
        # backward step
        if verbose:
            print('<<<<<<backward step')

        formula = 'target ~ ' + ' + '.join(included)

        log_reg = smf.logit(formula, new_data).fit_regularized(disp = 0)
        pvalues = log_reg.pvalues[1:]
        worst_pvalue = pvalues.max()
        worst_feature = pvalues.idxmax()

        if worst_pvalue > threshold_out:
            included.remove(worst_feature)
            changed = True
            if verbose:
                print(f'DROP {worst_feature}')
                
        # inversion check
        if inversion:
            if not changed:
                if verbose:
                    print('><><><inversion check')

                inversion_dict = {}

                for feat in included:
                    outside_risk = (default[ new_data[feat] == 0 ] == 1).mean() # P(bad|feature = 0)
                    inside_risk = (default[ new_data[feat] == 1 ] == 1).mean()  # P(bad|feature = 1)
                    if (inside_risk - outside_risk) * log_reg.params.loc[feat] <= 0:
                        inversion_dict[feat] = pvalues.loc[feat]                        

                if len(inversion_dict):
                    inverison_report = pd.Series(data = inversion_dict.values(), index = inversion_dict.keys())
                    worst_pvalue = inverison_report.max()
                    worst_feature = inverison_report.idxmax()
                    # included.remove(worst_feature)
                    included = []
                    new_data.drop(columns = worst_feature, inplace = True)
                    # clear_output()
                    changed = True
                    if verbose:
                        print(f'DROP {worst_feature}')

        if not changed:
            break

    return log_reg
