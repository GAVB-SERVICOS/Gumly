import functools
import types
import dill as pickle


class LocalWriter:

    def __init__(self, path):
        self.path = path

    def write(self, state):
        with open(self.path, 'wb') as f:
            pickle.dump(state, f)

    def read(self):
        try:
            with open(self.path, 'rb') as f:
                return pickle.load(f)
        except:
            return dict()


class CheckpointFlow:

    state_writers_constructors = {
        'local': LocalWriter
    }

    def __init__(self, state_path: str, writer: str = 'local'):

        self.fs = list()
        self.ckp_index = 0

        if not isinstance(writer, str):
            raise Exception('writer must be a string')

        available_writers = self.state_writers_constructors.keys()
        if writer not in available_writers:
            raise Exception(f'The available writers are {available_writers}')

        self.writer = self.state_writers_constructors[writer](state_path)

    def add_step(self, loader: types.FunctionType = None, saver: types.FunctionType = None):
        def decorator(f):

            @functools.wraps(f)
            def wrapper(state, load=False):
                if load and loader is not None:
                    loader(state)
                f(state)
                if saver is not None:
                    saver(state)

            self.fs.append(wrapper)
            return wrapper
        return decorator

    def check_point(self):
        state = self.writer.read()
        if 'checkpoint_index' in state:
            self.ckp_index = state['checkpoint_index']

    def run(self, state):
        self.check_point()
        for i in range(self.ckp_index, len(self.fs)):
            f = self.fs[i]
            f(state, load=i == self.ckp_index)

            state['checkpoint_index'] = i+1
            self.writer.write(state)

        state['checkpoint_index'] = 0
        self.writer.write(state)




if __name__ == '__main__':

    initial_state = {
        'a': 'baka'
    }

    def loader2(state):
        state['b'] = 10

    def saver(state):
        print(f"saver printing state={state}")

    cp = CheckpointFlow('state.pkl')

    @cp.add_step()
    def f1(state):
        print(f"f1 printing {state['a']}")
        state['d'] = 'D'
        return 10

    @cp.add_step()
    def f3(state):
        # raise Exception("This thing broke!")
        print("f3 is fine now")

    @cp.add_step(loader=loader2, saver=saver)
    def f2(state):
        print(f"f2 printing {state}")
        state['c'] = 4.5
        return -99

    cp.run(initial_state)