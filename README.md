# **MLutils**
The GAVB Machine Learning Utility library to improve apps!


## **Motivação e Descrição da Lib**

A Lib foi construida para otimizar e acelerar os algorítimos de machine learning que irão ser criados.


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

**Para o acelerador de redução de dimencionalidade**

para importar o acelerador:

```
from dimensionality_reduction import *

```
Abaixo segue o sumário dos parâmetros e cada método explicativo:



|   Parameter   |  Description  |    Default    |
| :---         |     :---:      |          ---: |
| `df_input`   | Array to compute SVD and PCA on, of shape (M,N)  | None  |
| `decomposition_method` | Choice of method | None |
| `K` | Number of singular values(SVD) and principal component analyis(PCA) to compute. Must be 1 <= k < min(A.shape) | None | 
| `explained_variance` | 0 < n_components < 1, select the number of components such that the 
        amount of variance that needs to be explained is greater than the percentage specified by n_components | None | 
| :---         | :---:          |           ---:|     



## **Release Notes**



