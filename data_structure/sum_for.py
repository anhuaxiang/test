import time
import numpy as np


a = range(10000000)
start = time.time()
print(sum(a))
print(time.time()-start)
print('*********************')
start = time.time()
add = 0
for i in a:
    add += i
print(add)
print(time.time()-start)