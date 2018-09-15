height=float(input('输入身高：'))
weight=float(input('输入体重：'))
x=weight/height/height
if x<=18.5:
	print('过轻')
elif x<=25:
	print('正常')
elif x<=28:
	print('过重')
elif x<=32:
	print('肥胖')
elif x>32:
	print('严重肥胖')