import getpass
from random import randint


def svc_login(user, passwd):
    print(user, passwd)
    if randint(1, 5) % 2 == 0:
        return True
    return False


user = getpass.getuser()
passwd = getpass.getpass('password:')

if svc_login(user, passwd):
    print('Yay!')
else:
    print('Bool')