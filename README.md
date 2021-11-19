# **MLutils**

[![APM](https://img.shields.io/apm/l/python?style=plastic)](https://github.com/GAVB-SERVICOS/mlutils/blob/feature/diego/LICENSE)


The GAVB Machine Learning Utility library to improve apps!


## **Motivação e Descrição da biblioteca**

A biblioteca foi construida para otimizar e acelerar o desenvolvimento de projetos de data science dentro da GAVB, utilizando de métodos que trazem maior velocidade e padronização aos trabalhos criados pelo time.


## **Geral de Funcionalidades (Links para os tutoriais)**

**A Lib está estruturada em :**

**- Códigos fontes**
Os aceleradores de utilidade para os projetos de machine learning.

**- Testes**
Os testes dos aceleradores feito no pytest para uma melhor qualidade do código.

**- Tutoriais**
Explicação com exemplos práticos o funcionamento de cada acelerador.

[Dimensionality Reduction](https://github.com/GAVB-SERVICOS/mlutils/blob/feature/diego/tutorial/tutorial_dimensionality_reduction.ipynb)

[Feature Engineering](https://github.com/GAVB-SERVICOS/mlutils/blob/feature/diego/tutorial/test_tutorial_feature_engineering_regression_hyperparams_tuning.ipynb)

[Movie Files](https://github.com/GAVB-SERVICOS/mlutils/blob/feature/diego/tutorial/tutorial_movie_files_create_dir.ipynb)

[Tuning Hyperparams](https://github.com/GAVB-SERVICOS/mlutils/blob/feature/diego/tutorial/tutorial_tuning_hyperparams.ipynb)

[Variable Treat](https://github.com/GAVB-SERVICOS/mlutils/blob/feature/diego/tutorial/tutorial_variable_treat.ipynb)

[Weighted Mean Absolute Percentage Error](https://github.com/GAVB-SERVICOS/mlutils/blob/feature/diego/tutorial/tutorial_weighted_mean_absolute_percentage_error.ipynb)


**Cada estutura está arquitetada em códigos de utilidade em :**
 
 - Redução de dimencionalidade
 - Seleção e engenharia de Features
 - Manipulação de arquivos
 - Otimização com Hiperparâmetos
 - Tratamento de Variáveis
 - Métricas do erro percentual do peso médio absoluto.


## **Como instalar**

Para Instalação da biblioteca:
```
pip install mlutils
```

## **Como usar**

**Para o acelerador de redução de dimencionalidade:**

Importando o acelerador:

```
from dimensionality_reduction import *

```
Abaixo segue o sumário dos parâmetros e cada método explicativo de redução de dimensionalidade:



|   Parameter   |  Description  |    Default    |    Type    |
| :---         |     :---:      |         :---: |        ---:|
| `df_input`   | Array to compute SVD and PCA on, of shape (M,N)  | None  | DataFrame |
| `decomposition_method` | Choice of method might be PCA or SVD | None |    str    |
| `K` | Number of singular values(SVD) and principal component analyis(PCA) to compute. Must be 1 <= k < min(A.shape) | None |    int    |
| `explained_variance` | 0 < n_components < 1, select the number of components| None |   float   |   


**Para o acelerador de seleção e engenharia de features:**

Importando o acelerador:

```
from feature_engineering import *

```

Abaixo segue o sumário dos parâmetros e cada método explicativo de seleção e engenharia de feature:



|   Parameter   |  Description  |    Default    |    Type    |
| :---         |     :---:      |         :---: |        ---:|
| `df`   | DataFrame pandas  | None  | DataFrame |
| `target` | Target variable | None |    str    |
| `num_feats` | The number of features that is wanted to remain after the process | None |    int    |
| `step` | The number steps| None |   int   | 
| `n_estimators` | The number of estimators for the training phase | 10 |   int   |
| `threshold_in` | Include a feature if its p-value < threshold_in | None |   float   |
| `threshold_out` | Exclude a feature if its p-value > threshold_out | None |   float   |
| `verbose` | Whether to print the sequence of inclusions and exclusions | None |   bool   |



**Para o acelerador de manipulação de arquivos:**

Importando o acelerador:

```
from movie_files_create_dir import *

```

Abaixo segue o sumário dos parâmetros e cada método explicativo de manipulação de arquivo:



|   Parameter   |  Description  |    Default    |    Type    |
| :---         |     :---:      |         :---: |        ---:|
| `source_dir`   | The source directory where are the files initially located | None  | str |
| `dest_dir` | The destiny directory where the files will be located | None |    str    |
| `save_dir` | Path directory where the files will be save | None |    str    |




**Para o acelerador de otimização com hiperparâmetros:**

Importando o acelerador:

```
from tuning_hyperparams impot *

```

Abaixo segue o sumário dos parâmetros e cada método explicativo de otimização com hiperparâmetros:



|   Parameter   |  Description  |    Default    |    Type    |
| :---         |     :---:      |         :---: |        ---:|
| `df`   | DataFrame pandas  | None  | DataFrame |
| `target` | Target variable | None |    str    |
| `parameters` | Dict that contains all the threshold given for optimization testing | None |    dict    |
| `algorithm` | Machine Learning algorithm used for fit the model| None |   class   | 
| `metric` | Metric used for the evaluation of the tests | None |   func   |
| `scoring_option` | Maximize or minimize objectives | None |   str   |
| `n_trials` | The of trials that the framework must perform | None |   int   |



**Para o acelerador de tratamento de variável:**

Importando o acelerador:

```
from variable_treat impot *

```

Abaixo segue o sumário dos parâmetros e cada método explicativo de tratamento de variável:



|   Parameter   |  Description  |    Default    |    Type    |
| :---         |     :---:      |         :---: |        ---:|
| `data`   | DataFrame pandas  | None  | DataFrame |
| `variables` | Variables to treat | None |    str or list    |
| `lower` | Method to select lower values | False |    bool    |
| `lower_percentile` | Minimum percentile threshold | None |   float   | 
| `upper` | Method to select upper values | False |   bool   |
| `upper_percentile` | Maximum percentile threshold | None |   float   |



**Para o acelerador de métricas do erro percentual do peso médio absoluto**

Importando o acelerador:

```
from weighted_mean_absolute_percentage_error impot *

```

Abaixo segue o sumário dos parâmetros e cada método explicativo de métricas do erro percentual do peso médio absoluto:



|   Parameter   |  Description  |    Default    |    Type    |
| :---         |     :---:      |         :---: |        ---:|
| `y_true`   | True target values  | None  | array |
| `y_pred` | Estimated target values | None |    array    |
| `weights` | Weights to use when averaging |  None  |    array    |


## **Release Notes**



