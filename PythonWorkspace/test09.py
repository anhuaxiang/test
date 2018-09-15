
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n
# def main():
#     foo('0')
#
# print(main())

# import logging
# logging.basicConfig(level=logging.INFO)
# n=0
# logging.info('n=%d'%n)
# print(10/0)

import pdb
s='0'
n=int(s)
pdb.set_trace()
print(10/n)



















