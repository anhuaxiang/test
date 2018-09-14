import re


def fun(string):
    for i in range(len(string)):
        if string[i] is not ' ':
            string = string[i:]
            break

    pattern = r'[-+]{0,1}[0-9]+'
    num_str = re.match(pattern, string)
    if not num_str:
        return 0
    num_str = int(num_str.group())
    num_str = min(num_str, pow(2, 31)-1)
    num_str = max(num_str, pow(-2, 31))
    return num_str


print(fun("   -42"))