def fun(a):
    if not check(a):
        return 0
    res = []
    par = []
    for i in a:
        if not par or par[0] == i:
            par.append(i)
        else:
            if ''.join(par) not in res:
                res.append(''.join(par))
            par = [i]
    if ''.join(par) not in res:
        res.append(''.join(par))
    a = ''

    for r in res:
        a = a + str(len(r)) + r[0] + ' '
    return a[:-1]


def check(a):
    result = True
    for i in a:
        if i > 'z' or i < 'a':
            result = False
            break
    return result

if __name__ == '__main__':
    a = input()
    print(fun(a))