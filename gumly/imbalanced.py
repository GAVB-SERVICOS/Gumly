from imblearn.over_sampling import RandomOverSampler
from imblearn.over_sampling import SMOTE
from imblearn.over_sampling import ADASYN
from imblearn.under_sampling import RandomUnderSampler
from imblearn.under_sampling import NearMiss
from imblearn.combine import SMOTEENN
from imblearn.combine import SMOTETomek


def oversampler(
    X, y, method: str, sampling_strategy: str = 'auto', sampler_obj=None, random_state=None, n_neighbors=5
):

    """Runs the chosen method of Over-sampling at imbalanced data
        and returns the balanced tuple with two arrays at index 0
        the values of input "X" transformed and at index 1 the values of "y".

    :param X : Matrix containing the data which have to be sampled.
    :type: array-like, dataframe, sparse matrix
    :param y : Corresponding label for each sample in X.
    :type: array-like of shape (n_samples)
    :param method : Choice method can be 'random', 'smote' and 'adasyn'
    :type: str
    :param sampler_obj : The instance of not fited imblearn object that contais the 'fit_resample' method.   .
    :type: obj, default=None
    :param sampling_strategy : Sampling information to resample the data set.
    :type: str, default = None
    :param random_state: Control the randomization of the algorithm.
    :type: int, default = None
    :param n_neighbors : Number of nearest neighbours to used to construct synthetic samples.
    :type: int, default = 5
    :return: One tuple with two arrays at index 0 the values of input "X" transformed and at index 1 the values of "y"
    oversampled.
    :rtype: Tuple
    """
    if hasattr(sampler_obj, "fit_resample"):
        return sampler_obj.fit_resample(X, y)
    else:

        if "random" == method.lower():
            sampler = RandomOverSampler(sampling_strategy=sampling_strategy, random_state=random_state)

        elif "smote" == method.lower():
            sampler = SMOTE(sampling_strategy=sampling_strategy, random_state=random_state, k_neighbors=n_neighbors)

        elif "adasyn" == method.lower():
            sampler = ADASYN(sampling_strategy=sampling_strategy, random_state=random_state, n_neighbors=n_neighbors)

        else:
            raise Exception(f"Method '{method}' not implemented!")

    return sampler.fit_resample(X, y)


def undersampler(
    X,
    y,
    method: str,
    sampler_obj=None,
    sampling_strategy: str = 'auto',
    random_state: int = None,
    n_neighbors=5,
    n_neighbors_ver3: int = 3,
    replacement: bool = False,
    n_jobs: int = -1,
):

    """Runs the chosen method of Under-sampling at imbalanced data
        and returns the balanced tuple with two arrays at index 0
        the values of input "X" transformed and at index 1 the values of "y".

    :param X : Matrix containing the data which have to be sampled.
    :type: array-like, dataframe, sparse matrix
    :param y : Corresponding label for each sample in X.
    :type: array-like of shape (n_samples)
    :param method : Choice method can be 'random' and 'nearmiss'.
    :type: str
    :param sampler_obj : The instance of not fited imblearn object that contais the 'fit_resample' method.   .
    :type: obj, default=None
    :param sampling_strategy : Sampling information to sample the data set.
    :type: str, default = 'auto'
    :param random_state: Control the randomization of the algorithm.
    :type: int, default = None
    :param n_neighbors : Size of the neighbourhood to consider to compute the average distance to the minority point
    samples.
    :type: int, default = 3
    :param n_neighbors_ver3 : NearMiss-3 algorithm start by a phase of re-sampling
    :type: int, default = 3
    :param replacement : Whether the sample is with or without replacement.
    :type: bool, default = False
    :param n_jobs : Number of CPU cores used during the cross-validation loop.
    :type: int, default = None
    :return: One tuple with two arrays at index 0 the values of input "X" transformed and at index 1 the values of "y"
    oversampled.
    :rtype: Tuple
    """
    if hasattr(sampler_obj, "fit_resample"):
        return sampler_obj.fit_resample(X, y)
    else:
        if "random" == method.lower():
            sample = RandomUnderSampler(
                sampling_strategy=sampling_strategy,
                random_state=random_state,
                replacement=replacement,
            )
        elif "nearmiss" == method.lower():
            sample = NearMiss(
                sampling_strategy=sampling_strategy,
                n_neighbors=n_neighbors,
                n_neighbors_ver3=n_neighbors_ver3,
                n_jobs=n_jobs,
            )
        else:
            raise Exception(f"Method '{method}' not implemented!")

    return sample.fit_resample(X, y)


def combine(
    X, y, method: str, sampling_strategy: str = 'auto', random_state=None, smote=None, enn=None, tomek=None, n_jobs=-1
):

    """Runs the chosen method Combination of over-and undersampling at imbalanced data
        and returns the balanced tuple with two arrays at index 0
        the values of input "X" transformed and at index 1 the values of "y".

    :param X : Matrix containing the data which have to be sampled.
    :type: array-like, dataframe, sparse matrix
    :param y : Corresponding label for each sample in X.
    :type: array-like of shape (n_samples)
    :param method : Choice method can be 'smoteenn' and 'smotetomek'.
    :type: str
    :param sampling_strategy : Sampling information to resample the data set.
    :type: str, default = 'auto'
    :param random_state: Control the randomization of the algorithm.
    :type: int, default = None
    :param smote :The smote object to use
    :type: sampler object, default = None
    :param enn : The EditedNearestNeighbours object to use.
    :type : sampler object, default = None
    :param tomek: The TomekLinks object to use.f not given, a TomekLinks object with sampling strategy='all' will
    be given.
    :type: sampler object, default = None
    :param n_jobs: Number of CPU cores used during the cross-validation loop.
    :type: int, default = None
    :return: One tuple with two arrays at index 0 the values of input "X" transformed and at index 1 the values
    of "y" oversampled.
    :rtype: Tuple
    """
    if "smoteenn" == method.lower():
        sampler = SMOTEENN(
            sampling_strategy=sampling_strategy, random_state=random_state, smote=smote, enn=enn, n_jobs=n_jobs
        )

    elif "smotetomek" == method.lower():
        sampler = SMOTETomek(
            sampling_strategy=sampling_strategy, random_state=random_state, smote=smote, tomek=tomek, n_jobs=n_jobs
        )

    else:
        raise Exception(f"Method '{method}' not implemented!")

    return sampler.fit_resample(X, y)
