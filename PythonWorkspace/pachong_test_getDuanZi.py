'''
Created on 2016年11月25日

@author: yanrujing
'''
import re
import urllib
import urllib.request

url = 'http://www.qiushibaike.com/hot/page/2/?s=4933582'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
try:
    req = urllib.request.Request(url,headers=headers)
    data = urllib.request.urlopen(req).read().decode('UTF-8')
    reg = r'<h2>(.*?)</h2>.*?<div class="content">.*?<span>(.*?)</span>'
    reD = re.compile(reg,re.S)
    list = re.findall(reD,data)
    for item in list:
        print('作者:'+item[0])
        print('内容:'+item[1])
        print('###########')
# r'<h2>(.*?)</h2>.*?<div class="content"><span>(.*?)</span>'  
except:
    print("******")
    