import numpy as np


def weighted_mean_absolute_percentage_error(y_true, y_pred, weights=None):

    """
    Implements the weighted MAPE metric.

    :param y_true: true target values
    :type: array-like of shape
    :param y_pred: estimated target values
    :type: array-like of shape
    :param weights: weights to use when averaging
    :type: array-like of shape. default = None
    :raise AssertionError: Predicted and true values have different shapes
    :raise AssertionError: Weights and true values have different shapes
    :raise AssertionError: Weights and predicted values have different shapes
    :raise AssertionError: Weights cannot be negative
    :raise AssertionError: Weights cannot be all equal to zero
    :return: float number
    :rtype: float

    """

    if not weights:
        weights = np.ones_like(y_true)

    y_true = np.asarray(y_true).reshape(-1)
    y_pred = np.asarray(y_pred).reshape(-1)
    weights = np.asarray(weights).reshape(-1)

    assert y_true.shape == y_pred.shape, "Predicted and true values have different shapes."
    assert y_true.shape == weights.shape, "Weights and true values have different shapes."
    assert y_pred.shape == weights.shape, "Weights and predicted values have different shapes."
    assert np.all(weights > 0), "Weights cannot be negative."
    assert np.sum(weights) != 0, "Weights cannot be all equal to zero."

    weights = weights / np.sum(weights)

    num = np.sum(weights * (np.abs(y_true - y_pred)))
    den = np.sum(weights * y_true)

    return num / den
