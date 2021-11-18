from sklearn.decomposition import PCA
from scipy.sparse.linalg import svds

# TODO: make argument explained_variance works in PCA.
# One possible way to solve this, is by using the argument from the Class PCA: svd_solver='arpack'.
def dimensionality_reduction(
    df_input,
    decomposition_method: str = None,
    k: int = None,
    explained_variance: float = None,
):
    """
    Implements methods for dimensionality reduction.
    
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
    :raise ValueError: K and explained_variance must be defined.
    :raise TypeError: explained_variance must be a float.
    :raise ValueError : explained_variance must be in the interval (0..1) and k 
        or explained_variance must be defined
    :raise NotImplementedError: Model implemented yet. Available names: 'SVD', 'PCA'
    :return: Input data with reduced dimensions
    :rtype: numpy.ndarray

    """
    if k is None and explained_variance is None:
        raise ValueError(f"k and explained_variance must be defined")

    if decomposition_method == "SVD":
        # Implements SVD for reducing dimensionality
        df_input = df_input.astype(float)
        u, s, vt = svds(df_input, k=k)
        return u

    elif decomposition_method == "PCA":
        if k is not None:
            # Implements PCA for reducing dimensionality
            u = PCA(k).fit_transform(df_input)
        elif explained_variance is not None:

            if not isinstance(explained_variance, float):
                raise TypeError(
                    f"explained_variance must be a float, but its value passed was {explained_variance}."
                )
            if explained_variance <= 0 or explained_variance >= 1:
                raise ValueError(f"explained_variance must be in the interval (0..1)")

            u = PCA(explained_variance).fit_transform(df_input)
        return u

    else:
        raise NotImplementedError(
            "Model implemented yet. Available names: 'SVD', 'PCA'."
        )
