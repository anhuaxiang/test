import math

a, b = int(input()), int(input())


s_sum = 0
for i in range(1, b+1):
    s_sum += a
    a = math.sqrt(a)

print(round(s_sum, 2))
