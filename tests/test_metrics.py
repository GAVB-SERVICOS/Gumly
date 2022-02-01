import pytest

from gumly.metrics import weighted_mean_absolute_percentage_error


def test_wmap():

    y_true = [3, -0.5, 2, 7]
    y_pred = [2.5, 0.0, 2, 8]
    assert weighted_mean_absolute_percentage_error(y_true, y_pred) == 0.17391304347826086


def test_wmap_weight():

    y_true = [3, -0.5, 2, 7]
    y_pred = [2.5, 0.0, 2, 8]

    assert weighted_mean_absolute_percentage_error(y_true, y_pred, weights=[2, 1, 1, 3]) == 0.15789473684210525


def test_weighted_mean_absolute_percentage_error_predict_true_shape():
    with pytest.raises(AssertionError) as ex:
        y_true = [3, -0.5, 2, 7]
        y_pred = [2.5, 0.0, 2, 8, 9]
        weighted_mean_absolute_percentage_error(y_true, y_pred)
        assert str(ex) == "Predicted and true values have different shapes."


def test_weighted_mean_absolute_percentage_error_predict_true_weights_shape():
    with pytest.raises(AssertionError) as ex:
        y_true = [3, -0.5, 2, 7]
        y_pred = [2.5, 0.0, 2, 8]
        weighted_mean_absolute_percentage_error(y_true, y_pred, weights=[1, 2])
        assert str(ex) == "Weights and true values have different shapes."


def test_weighted_mean_absolute_percentage_error_predict_true_weights_less_zero():
    with pytest.raises(AssertionError) as ex:
        y_true = [3, -0.5, 2, 7]
        y_pred = [2.5, 0.0, 2, 8]
        weighted_mean_absolute_percentage_error(y_true, y_pred, weights=[-1, -2, -3, -4])
        assert str(ex) == "Weights cannot be negative."


def test_weighted_mean_absolute_percentage_error_predict_true_weights_equal_zero():
    with pytest.raises(AssertionError) as ex:
        y_true = [3, -0.5, 2, 7]
        y_pred = [2.5, 0.0, 2, 8]
        weighted_mean_absolute_percentage_error(y_true, y_pred, weights=[0, 0, 0, 0])
        assert str(ex) == "Weights cannot be all equal to zero."
