from mlutils.variable_treat import *
import numpy as np
import pytest
import pandas as pd


def test_vt():

    df2 = pd.DataFrame(
        np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"]
    )

    assert variable_treat(
        df2, "a", lower=True, lower_percentile=1.0, upper=True, upper_percentile=2.0
    ) == [0, 1, 2]


test_vt()


def test_passes():
    with pytest.raises(NotImplementedError) as ex:
        df2 = pd.DataFrame(
            np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=["a", "b", "c"]
        )
        variable_treat(
            df2,
            "a",
            lower=False,
            lower_percentile=1.0,
            upper=False,
            upper_percentile=90.0,
        )
        assert ex.message == "One of those paramns must be True"
