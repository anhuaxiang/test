from functools import wraps
import inspect


def optional_debug(func):
    print(inspect.getfullargspec(func))
    if 'debug' in inspect.getfullargspec(func).args:
        raise TypeError('debug argument already defined')

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print('Calling', func.__name__)
        return func(*args, **kwargs)

    return wrapper


@optional_debug
def a(x):
    pass


@optional_debug
def b(x, y):
    pass


@optional_debug
def c(x, y, z):
    pass


a(1, debug=True)
b(1, 2)
c(1, 2, 3)
