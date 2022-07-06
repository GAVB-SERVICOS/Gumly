import functools
import types
import dill as pickle


class LocalStateHandler:
    """
    This class is responsible for writing and reading the contents of the state of
    a program (i.e. a set of small variables) into and from a file in the local
    filesystem. The state is defined as a dictionary and it is serialized in
    the file with the Dill library.
    """

    def __init__(self, path: str):
        """
        Creates a new LocalStateHandler object.

        :param path: The local path to where the state file will be stored
        :type: String

        :return: The new object
        :rtype: gumly.checkpoint_flow.LocalStateHandler

        """
        self.path = path

    def write(self, state: dict):
        """
        Writes the given state in the local file, whose path should have
        been passed in the constructor.

        The lib dill is used to serialize the dictionary object and write it
        into the file. Please learn about dill's limitations here:
        https://pypi.org/project/dill/

        :param state: A set of key-value pairs, which represent a program state
        :type: Dictionary

        """
        with open(self.path, 'wb') as f:
            pickle.dump(state, f)

    def read(self) -> dict:
        """
        Reads the content of a state from the local file, whose path should have
        been passed in the constructor.

        The lib dill is used to serialize the dictionary object and write it
        into the file. Please learn about dill's limitations here:
        https://pypi.org/project/dill/

        :return: The content of the state from the file
        :rtype: Dictionary

        """
        try:
            # try to read the content of the file and return it
            with open(self.path, 'rb') as f:
                return pickle.load(f)
        except Exception:
            # if anything bad happens, return an empty dict
            return dict()


class CheckpointFlow:
    """
    This class is responsible for creating and running a series of functions
    while checkpoint along the way, so that if something goes wrong in any
    function, when re-running the series, it can start from the function which
    raised the error, instead of running everything all over again.
    """

    # global variable that tells which state handlers are implemented
    state_handler_constructors = {
        'local': LocalStateHandler
    }

    def __init__(self, state_path: str, handler: str = 'local'):
        """
        Creates a new CheckpointFlow object.

        :param state_path: The path to where the state file will be stored.
            The interpretation of the path depends on the state handler
        :type: String
        :param handler: The name of the state handler. i.e. the key of
            state_handler_constructors field that corresponds to the chosen
            handler. Default value is "local"
        :type: String

        :raise TypeError: handler must be a string
        :raise NotImplementedError: The available handlers are [...]

        :return: The new object
        :rtype: gumly.checkpoint_flow.CheckpointFlow

        """

        # initialize the list of functions
        self.fs = list()
        # initialize the checkpoint index
        self.ckp_index = 0

        # check if the handler is a string
        if not isinstance(handler, str):
            raise TypeError('handler must be a string')

        # check if the given handler name is acceptable
        available_handlers = self.state_handler_constructors.keys()
        if handler not in available_handlers:
            raise NotImplementedError(f'The available handlers are {available_handlers}')

        # initialize the state handler object with the given path
        self.handler = self.state_handler_constructors[handler](state_path)

    def add_step(self, load: types.FunctionType = None, save: types.FunctionType = None):
        """
        This method is a decorator. It adds a function into the list of functions and
        optionally wraps it with a load ad save functions for large datasets.

        The main function should have two arguments "state" and "data", in this exact
        order. They receive the set of small variables and the large data, respectively.
        This function must insert all new variables and data, as well as modified values,
        back into the "state" and "data" objects, so that the next main function in the
        sequence may receive them.

        The load function must have one argument named "state", so that it can use
        some variables in order to retrieve the data. And it must return a dictionary.

        The save function must have these two arguments, named "state" and "data",
        containing everything it needs to save the desired data in the proper location.

        :param load: A function that should read large datasets and make them available
            to the main function
        :type: Function
        :param save: A function that should save large processed datasets, so the next
            main functions would be able to access and use them
        :type: Function

        :return: The decorator function
        :rtype: Decorator

        """
        def decorator(f):

            @functools.wraps(f)
            def wrapper(state: dict, should_load: bool = False, data: dict = dict()):
                """
                Wraps the given function with a load and save functions to
                interact with large amounts of data, and with a load argument
                to tell whether the load function should be executed.

                :param state: A set of variables values, necessary to the main function
                :type: Dictionary
                :param should_load: Whether the load function should be executed.
                    Default value is False
                :type: Boolean
                :param data: The large dataset, if any. If should_load is True, this is
                    ignored and the data returned by the load function is used instead
                :type: Dictionary

                :raise TypeError: Data should be a dictionary

                :return: The processed data
                :rtype: Dictionary

                """
                # if data is not a dict, raise an error
                if type(data) is not dict:
                    raise TypeError(f"Data should be a dictionary, even an empty one. But it was a {type(data)}")

                # if loading large data is necessary, ...
                if should_load and load is not None:
                    # load it into memory
                    data.update(load(state))
                # run the main function with the given state and data
                f(state, data)
                # if some save function is provided, ...
                if save is not None:
                    # run it to save the large processed data
                    save(state, data)
                # return the processed data
                return data

            # add the wrapped function in the list of main functions
            self.fs.append(wrapper)
            return wrapper
        return decorator

    def check_point(self) -> dict:
        """
        Reads the checkpoint state, identifies the current
        checkpoint index and return the state itself.

        :return: The state, i.e. set of variables in a dict
        :rtype: Dictionary
        """
        # read the state file
        state = self.handler.read()
        # if the checkpoint index info is present, ...
        if 'checkpoint_index' in state:
            # update the internal index
            self.ckp_index = state['checkpoint_index']

        # return the state itself
        return state

    # TODO: be able to select the checkpoint index to begin with
    def run(self, state: dict = None, load_policy: str = 'first only', checkpoint: int = None):
        """
        Runs the sequence of main functions, managing the checkpoints and
        the large data.

        :param state: The initial state. If there is a checkpoint corresponding
            to somewhere in the middle of the sequence, this value is ignored
            and the state is read from the file. If it's not given, an attempt
            to read the state from the file is made
        :type: Dictionary
        :param load_policy: The name of the large data loading policy. It can be
            "first only", which means that only the load function of the first
            executed main function, will be executed. Or "always", which means
            every load function will be executed. Optionally, it can be a list of
            booleans, telling whether the load of the main function with the
            corresponding list index, should be executed or not
        :type: String or List
        :param checkpoint: The index of the main function that should start the
            execution sequence
        :type: Integer

        :raise ValueError: The load_policy as a list has the wrong number of elements
        :raise TypeError: The load_policy is neither a string nor a list.
            Or the checkpoint is not an integer

        """
        # try to read the state from the file and get the checkpoint index info
        temp_state = self.check_point()
        # use the state form the file if there's no given state, or
        # if there is a checkpoint from the file somewhere in the middle of the sequence
        # otherwise, use the given state
        state = temp_state \
            if state is None or (
                'checkpoint_index' in temp_state and
                temp_state['checkpoint_index'] > 0
            ) \
            else state
        # initialize the data as None, it will be loaded from a load function
        data = dict()

        # use the given checkpoint index, if any
        if checkpoint is not None:
            # TODO: use some new value validation functions
            if type(checkpoint) is not int:
                raise TypeError(f"checkpoint should be an integer, but was found to be a {type(checkpoint)}.")



        # Handle the policy choice and map it to a list of booleans
        # initialize the policy list with all false
        policy = [False for i in range(len(self.fs))]
        # if the given policy is a name, ...
        if type(load_policy) is str:

            if load_policy == 'first only':
                # if there is a checkpoint index, ...
                if 'checkpoint_index' in state:
                    # set the index of the checkpoint to load
                    policy[state['checkpoint_index']] = True
                else:
                    # set the first one to load
                    policy[0] = True

            elif load_policy == 'always':
                # set all load function to be executed
                policy = [True for i in len(self.fs)]

        # if a list was given, ...
        elif type(load_policy) is list:
            # the length of the list must be equal to the amount of main functions
            if len(load_policy) != len(self.fs):
                # otherwise, raise an error
                raise ValueError(f"When the load_policy is a list it should have the same"
                                 f" number of elements as the number of main functions in"
                                 f" the sequence, which is {len(self.fs)}, but it has"
                                 f" {len(load_policy)} elements.")
            # use the given list
            policy = load_policy
        else:
            # if the policy is neither a string nor a list, raise an error
            raise TypeError(f"load_policy must be either a string a list of booleans, but"
                            f" it was found to be a {type(load_policy)}.")

        # for each index, starting by the checkpoint, ...
        for i in range(self.ckp_index, len(self.fs)):
            # run the wrapped main function
            data = self.fs[i](
                state,
                should_load=policy[i],
                data=data
            )
            # update the checkpoint index
            state['checkpoint_index'] = i+1
            # save the checkpoint state
            self.handler.write(state)

        # when all functions finished executing with no error, set the
        # checkpoint index to the first function
        state['checkpoint_index'] = 0
        # save the final checkpoint
        self.handler.write(state)


if __name__ == '__main__':
    initial_state = dict(
        a='value of A'
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
        data['y'] = [10, 20, 30]


    def loader3(state):
        print("loader3")
        return {'z': ['A', 'B', 'C']}


    def saver3(state, data):
        print(f"saver3 printing data={data}")


    @cp.add_step(load=loader3, save=saver3)
    def f3(state, data):
        print(f"f3 printing state: {state}")
        print(f"f3 printing data: {data}")
        state['c'] = 4.5
        return -99


    cp.run(initial_state)