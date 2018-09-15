# try:
#     f=open('test.txt','r')
#     print(f.read())
# finally:
#     if f:
#         f.close()

# with open('test1.txt','r') as f:
#     print(f.read())

# with open('test.jpg','rb') as f:
#     print(f.read())

# f=open('G:/PythonWorkspace/test.txt','w')
# f.write('hello world')
# f.close()

# with open('test.txt','w') as f:
#     f.write('hello xiaoyan')

from io import StringIO
f=StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue())

f1=StringIO('hello!\nHi!\nGoodbye!')
while(True):
    s=f1.readline()
    if s=='':
        break
    print(s.strip())











