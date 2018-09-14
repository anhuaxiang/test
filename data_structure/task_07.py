def fun_2(mul, res):
    if not isinstance(mul, list):
        res.append(mul)
    else:
        for each in mul:
            fun_2(each, res)


def fun_1(s, n):
    result = []
    res = []
    for i in range(n):
        res.append([])
    for i in range(len(s)):
        index = i % (2*n-2)
        if index < n:
            res[index].append(s[i])
        else:
            res[2*n-index-2].append(s[i])
    for i in res:
        result += i
    return ''.join(result)

r = fun_1('PAYPALISHIRING', 3)
print(r)