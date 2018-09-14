def fun(n):
    flag = True
    binary = []
    while n > 0:
        binary.append(n%2)
        n //= 2
    binary.reverse()
    i, j = 0, len(binary)-1
    while i < j:
        if binary[i] == binary[i+1] or binary[j] == binary[j-1]:
            flag = False
            break
        i += 1
        j -= 1
    return flag

print(fun(11))