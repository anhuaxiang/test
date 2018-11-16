import time
from functools import wraps


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timer
def countdown(n: int):
    """
    counts down
    :param n:
    :return:
    """
    while n > 0:
        n -= 1


countdown(100000)
print(countdown.__name__)
print(countdown.__doc__)
print(countdown.__annotations__)
countdown.__wrapped__(1000)