import copy
def fun(x):
    if x < 0:
        return False
    y = x
    res = 0
    while y > 0:
        b = y % 10
        res = res * 10 + b
        y //= 10
    return res == x


def fun_2(x):
        if x < 0:
            return False
        x = list(str(x))
        y = x
        return x == list(reversed(y))
print(fun_2(123211))