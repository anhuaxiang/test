# python3


# def triangles():
#     p = [1]
#     while True:
#         yield p
#         p = [1] + [p[i] + p[i+1] for i in range(len(p)-1)] + [1]


# if __name__ == '__main__':
#     n = int(input())
#     # m = int(input())
#     for t in triangles():
#         print(t)
#         n -= 1
#         if n == 0:
#             # print(t[m-1])
#             break


n = input()
n = int(n)
arr = [[0] * n for i in range(n)]


def d(array, x, y, start, n):
    if n <= 0:
        return 0
    if n == 1:
        array[x][y] = start
        return 0
    for i in range(n):
        array[x][y + i] = start
        start += 1
    for i in range(n - 1):
        array[x + 1 + i][y + n - 1] = start
        start += 1
    for i in range(n - 1):
        array[x + n - 1][y + n - 2 - i] = start
        start += 1
    for i in range(n - 2):
        array[x + n - 2 - i][y] = start
        start += 1
    d(array, x + 1, y + 1, start, n - 2)


a = d(arr, 0, 0, 1, n)
l = len(str(n * n)) + 1
format = ('%' + str(l) + 'd') * n
# print(arr)
for i in arr:
    print(format % tuple(i))
