string = 'addDoFun'
result = []
for i in string:
    if i in ['A', 'B', 'C', 'D', 'E', 'F']:
        result.append('_')
    result.append(i.lower())
print(''.join(result))
