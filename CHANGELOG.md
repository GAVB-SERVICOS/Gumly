# CHANGELOG

This file follows [semantic versioning 2.0.0](https://semver.org/). Given a version number MAJOR.MINOR.PATCH, increment
the:

- **MAJOR** version when you make incompatible API changes,
- **MINOR** version when you add functionality in a backwards compatible manner, and
- **PATCH** version when you make backwards compatible bug fixes.

As a heuristic:

- if you fix a bug, increment the PATCH
- if you add a feature (add keyword arguments with default values, add a new object, a new mechanism for parameter setup
  that is backwards compatible, etc.), increment the MINOR version
- if you introduce a breaking change (removing arguments, removing objects, restructuring code such that it affects
  imports, etc.), increment the MAJOR version

The general format is:

```

# VERSION - DATE (dd/mm/yyyy)
### Features and improvements
- module alpha.py
  - A: brief description of A.
  - B: brief description of B.
- module beta.py
  - C: brief description of C.

### Fixes
- module alpha.py:
  - New fixed behavior #1 
  - New fixed behavior #2

### Deprecated
- module alpha.py
  - function A
  - argument B of function C

```

# 1.1.0 - DATE (05/07/2022)

### Features

- module geo_location.py
  - city_to_region: Fill the region through the city returning a pd.series.
  - city_to_microregion: Fill the microregion through the city returning a pd.series.
  - city_to_mesoregion: Fill the mesoregion through the city returning a pd.series.
  - city_to_immediate_region: Fill the immediate region through the city returning a pd.series.
  - city_to_intermediary_region:  Fill the intermediary region through the city returning a pd.series.
  - state_to_region: Fill the region through the state returning a pd.series.
  - cep_to_state: Fill the state through the cep returning a pd.series.
  - cep_to_region: Fill the region through the cep returning a pd.series.
  - ibge_to_city: Fill the city through ibge id returning a pd.series.
  - city_to_ibge: Fill the ibge id through the city returning a pd.series.

# 1.0.0 - DATE (01/02/2022)

### Features

- module dimencionality_reduction.py
  - dimencionality_reduction: Wrapper for two well-know methods, PCA and svds.
  
- module feature_engineering.py
  - split_features_and_target: Separates the features and the target columns into two new dataframes.
  - feature_selection_filter: Feature selection using filter technique and chi2 values.
  - feature_selection_wrapper: Feature selection using wrapper technique and LogisticRegression.
  - feature_selection_embedded: Feature selection using embedded technique and LightGBMClassifier.
  - feature_selection_stepwise: Perform a forward-backward feature selection based on p-value from statsmodels.api.OLS.
  - feature_selection_f_regression: Perform a f_regression feature selection based on p-value.
  - feature_selection_mutual_information: Perform a mutual_info_regression feature selection.
  - ordering_filter: Analyzes the records of all given variables and returns their indexes.

- module files.py
  - create_dir: Creates a directory if it doesn't exist.
  - move_files: Moves the files from source_dir to dest_dir.

- module hyperparameter_tuning.py
  - hyperparameter_tuning: Perform hyperparameters optimization using optuna framework for the chosen technique.

- module metrics.py
  - weighted_mean_absolute_percentage_error: Implements the weighted MAPE metric.

- module value_validation.py
  - check_number: This function returns True if the first argument is a number and it lies between the next two arguments. Othwerise, returns False.
  - assert_check_number: This function uses check_number function and it will raise an exception if returns False.
  - check_dtypes: Verify the list of types.
  - assert_check_dtypes: Verify dataframe columns dtypes.
