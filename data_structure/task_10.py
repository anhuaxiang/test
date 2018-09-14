def int_to_roman(num):
    c = {0: ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
         1: ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"],
         2: ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
         3: ["", "M", "MM", "MMM"]}
    roman = [c[3][num // 1000 % 10], c[2][num // 100 % 10], c[1][num // 10 % 10], c[0][num % 10]]
    s = ''
    for i in roman:
        s += i
    return s


def roman_to_int(s):
    sum = 0
    convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    for i in range(len(s) - 1):
        if convert[s[i]] < convert[s[i + 1]]:
            sum -= convert[s[i]]
        else:
            sum += convert[s[i]]
    sum += convert[s[-1]]
    return sum


print(roman_to_int('VI'))