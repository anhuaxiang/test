# -*- coding: utf-8 -*
import urllib2
data = urllib2.urlopen('https://www.taobao.com').read().decode('UTF-8')
print data
# print '你好！'