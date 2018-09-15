# python3


def triangles():
    p = [1]
    while True:
        yield p
        p = [1] + [p[i] + p[i + 1] for i in range(len(p) - 1)] + [1]


def is_val(string):
    f = True
    for each in string:
        if each not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', 'E', '+']:
            f = False
            break
    return f


def is_int(string):
    f = is_val(string)
    if f:
        l = string.split('E+')
        if len(l) == 1:
            pass
        elif len(l) == 2:
            pass
        else:
            f = False
    return f


if __name__ == '__main__':
    print(is_int('1.23E+10'))

# if __name__ == '__main__':
#     n = int(input())
#     m = int(input())
#     for t in triangles():
#         n -= 1
#         if n == 0:
#             print(t[m-1])
#             break
import numpy as np

np.random.randint(1, 2, [10, 10])
np.random.randint(0, 100, [10, 10])
np.random.uniform(0, 100, [10, 10])
np.random.normal(1.5, 0.1, [10, 10])
np.zeros()
np.random.rand(10)

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
stus_score > 80  # 大于80
stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
np.where(stus_score < 80, 0, 90)  # 大于80替换为0，否则替换为90
result = np.amax(stus_score, axis=0)  # 列的最大值
result = np.amax(stus_score, axis=1)  # 行的最大值
