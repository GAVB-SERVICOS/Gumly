import pytest

from gumly.checkpoint_flow import (
    CheckpointFlow
)


def test_argument_validation_check_number():

    initial_state = dict(
        a = 'value of A'
    )

    cp = CheckpointFlow('state.pkl')

    def loader(state):
        print("loader")
        return {'x': [1, 2, 3]}

    def saver(state, data):
        print(f"saver printing data={data}")

    @cp.add_step(load=loader, save=saver)
    def f1(state, data):
        print(f"f1 printing state: {state}")
        print(f"f1 printing data: {data}")
        state['d'] = 'D'
        return 10

    @cp.add_step()
    def f2(state, data):
        # raise Exception("This thing broke!")
        print(f"f2 printing state: {state}")
        print(f"f2 printing data: {data}")

    def loader3(state):
        print("loader3")
        return {'y': [10, 20, 30]}

    def saver3(state, data):
        print(f"saver3 printing data={data}")

    @cp.add_step(load=loader3, save=saver3)
    def f3(state, data):
        print(f"f3 printing state: {state}")
        print(f"f3 printing data: {data}")
        state['c'] = 4.5
        return -99

    cp.run(initial_state)

test_argument_validation_check_number()

'''
def test_argument_validation_check():

    lower_percentil = 1

    assert_check_number(lower_percentil, 0, 1.0, "lower_percentil")


def test_argument_validation_error():
    with pytest.raises(AssertionError):

        lower_percentil = -1

        assert_check_number(lower_percentil, 0, 1.0, "lower_percentil")


def test_check_dtypes():

    x = pd.DataFrame({'a': [1, 2, 3], 'b': ['1', '2', '3']})

    with pytest.raises(ValueError):
        check_dtypes(x, [])

    assert None == check_dtypes(x, ['float64'])


def test_assert_check_dtypes_error():

    x = pd.DataFrame({'a': [1, 2, 3], 'b': ['1', '2', '3']})
    y = pd.DataFrame({'a': [1, 2, 3], 'b': [1.0, 1.2, 3.0]})

    with pytest.raises(AssertionError):

        y = pd.DataFrame({'a': [1, 2, 3], 'b': [1.0, 1.2, 3.0]})

        assert_check_dtypes(y, ['float64'])

    assert None == assert_check_dtypes(x, ['float64'])
'''