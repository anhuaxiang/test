import re


def fun_2(string):
    result = []
    for i in string:
        if i in ['A', 'B', 'C', 'D', 'E', 'F']:
            result.append('_')
        result.append(i.lower())
    return ''.join(result)


def fun_1(string, sep='_'):
    pattern = re.compile(r'([A-Z])')
    sub = re.sub(pattern, sep + r'\1', string).lower()
    return sub


def fun_3(string, sep='_'):
    result = [string[0].lower(), ]
    for each in string[1:]:
        if 'A' <= each <= 'Z':
            result.append(sep)
        result.append(each.lower())
    return ''.join(result)


print(fun_3('PersonNamePattern'))
