def fun(*args):
    if not args:
        return ''
    res = ''
    list_count = len(args)
    min_lens = min([len(i) for i in args])
    for i in range(min_lens):
        char = args[0][i]
        flag = 1
        for j in range(list_count-1):
            if args[j+1][i] != char:
                flag = 0
                break
        if not flag:
            break
        res += args[0][i]
    return res

a = ["flower", "flow", "flight"]
b = ["dog", "racecar", "car"]
print(fun(*[]))