from typing import Any

from scipy.sparse.linalg import svds
from sklearn.decomposition import PCA


def dimensionality_reduction(
    df_input,
    decomposition_method: str = None,
    k: int = None,
    explained_variance: float = None,
    **kwargs: Any,
):
    """
    Runs the chosen method of dimensionality reduction in the input data (df_input)
     and returns the reduced one.

    :param df_input: sparse matrix
    :type: Array to compute SVD and PCA on, of shape (M,N)
    :param decomposition_method: Choice of method
    :type: str, default = None
    :param K: Number of singular values(SVD) and principal component analyis(PCA) to compute.
        Must be 1 <= k < min(A.shape)
    :type: int, default = None
    :param explained_variance: 0 < n_components < 1, select the number of components such that the
        amount of variance that needs to be explained is greater than the percentage
        specified by n_components
    :type: float, default = None
    :params kwargs: Extra parameters passed to the selected method's base function
    :type: dict
    :raise ValueError: K and explained_variance must be defined.
    :raise TypeError: explained_variance must be a float.
    :raise ValueError : explained_variance must be in the interval (0..1) and k
        or explained_variance must be defined
    :raise NotImplementedError: Model implemented yet. Available names: 'SVD', 'PCA'
    :return: Input data with reduced dimensions
    :rtype: numpy.ndarray

    """
    if k is None and explained_variance is None:
        raise ValueError("k and explained_variance must be defined")

    if decomposition_method == "SVD":

        df_input = df_input.astype(float)
        u, _, _ = svds(df_input, k=k, **kwargs)
        return u

    elif decomposition_method == "PCA":
        if k is not None:

            u = PCA(k, **kwargs).fit_transform(df_input)
        elif explained_variance is not None:

            if not isinstance(explained_variance, float):
                raise TypeError(f"explained_variance must be a float, but its value passed was {explained_variance}.")
            if explained_variance <= 0 or explained_variance >= 1:
                raise ValueError("explained_variance must be in the interval (0..1)")

            u = PCA(explained_variance, svd_solver='full', **kwargs).fit_transform(df_input)
        return u

    else:
        raise NotImplementedError("Method not implemented yet. Available names: 'SVD', 'PCA'.")
