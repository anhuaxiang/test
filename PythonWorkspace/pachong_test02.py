'''
Created on 2016年11月22日

@author: yanrujing
'''
import urllib.request
from test.test_urllib import urlopen
url = 'http://www.douban.com'
req = urllib.request.Request(url, headers = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
openr = urllib.request.urlopen(req)
data = openr.read()
print(data.decode())