n = 10
for i in range(n):
    result = []
    for j in range(n-i-1):
        result.append(' ')
    for j in range(i+1):
        result.append('*')
        result.append(' ')
    print(''.join(result))
