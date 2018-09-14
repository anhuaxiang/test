
def reverse(x):
    if x > 0:
        x = int(str(x)[::-1])
    else:
        x = str(x)[::-1]
        x = x[:-1]
        x = (-1) * int(x)

    if x > pow(2, 31) -1 or x < pow(-2, 31):
        return 0
    return x
print(reverse(1534236469))