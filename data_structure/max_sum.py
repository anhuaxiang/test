
def fun(l):
    max_sum = -9999
    for i in range(len(l)):
        for j in range(i+1, len(l) + 1):
            max_sum = max(max_sum, sum(l[i:j]))
    return max_sum


def fun_2(l):
    max_sum = -9999
    temp = 0
    for i in range(len(l)):
        temp = max(temp + l[i], l[i])
        max_sum = max(max_sum, temp)
    return max_sum


if __name__ == '__main__':
    l = [-4, -3, -56, -15, -34, -50, -14, -4]
    print(fun(l))
    print(fun_2(l))