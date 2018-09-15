# python 

n = input()
arr = [[0]*n for i in range(n)]
def d(arr, x, y, start, n):
    if n<=0:
        return 0
    if n == 1:
        arr[x][y] = start
        return 0
    for i in range(n):
        arr[x][y+i] = start
        start += 1
    for i in range(n-1):
        arr[x+1+i][y+n-1] = start
        start += 1
    for i in range(n-1):
        arr[x+n-1][y+n-2-i] = start
        start += 1
    for i in range(n-2):
        arr[x+n-2-i][y] = start
        start += 1
    d(arr, x+1, y+1, start, n-2)
a = d(arr, 0, 0, 1, n)
l = len(str(n*n))+1
format = ('%'+str(l)+'d')*n
print arr
for i in arr:
    print format%tuple(i)
    
    