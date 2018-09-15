'''
Created on 2016年11月21日

@author: yanrujing
'''
import urllib.request
url = 'http://www.douban.com/'
webPage=urllib.request.urlopen(url)
data = webPage.read()
data = data.decode('UTF-8')
print(data)
print('***************************')
print(type(webPage))
print('***************************')
print(webPage.geturl())
print('***************************')
print(webPage.info())
print('***************************')
print(webPage.getcode())