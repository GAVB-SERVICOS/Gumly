from time import time


def get_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time()
        r = func(*args, **kwargs)
        print(f'Time to execute {str(func).split()[1]}: {round((time() - start), 4)}')
        return r
    return wrapper