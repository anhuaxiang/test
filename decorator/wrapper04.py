from functools import wraps, partial


def add(a, b, c):
    return a + b + c


add_new = partial(add, 1)

print(add_new(2, 3))