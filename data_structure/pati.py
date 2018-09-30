def fun(n):
    if n == 1 or n == 0:
        return 1
    return fun(n-1) + fun(n-2)

print(fun(20))


def fun_1(n):
    if n <= 2:
        return n
    f = 1
    s = 2
    res = 0
    for i in range(2, n):
        res = f + s
        f = s
        s = res
    return res
print(fun_1(20))


def fun_2(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    return b
print(fun_2(20))


def plus_one(digits):
    digits.reverse()
    flag = 1
    for i in range(len(digits)):
        if flag + digits[i] > 9:
            digits[i] = 0
            flag = 1
        else:
            digits[i] += 1
            flag = 0
            break
    if flag:
        digits.append(1)
    digits.reverse()

a = [9, 9, 9]
print(a)
plus_one(a)
print(a)


def length_of_last(s=''):
    while True and s:
        if s[-1] == ' ':
            s = s[:-1]
        else:
            break
    sum = 0
    index = len(s)-1
    for i in s:
        if s[index] == ' ':
            break
        sum += 1
        index -= 1
    return sum

print(length_of_last(' '))