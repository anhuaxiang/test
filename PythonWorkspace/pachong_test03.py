'''
Created on 2016年11月25日

@author: yanrujing
'''

import sys
import os
import re
import urllib.request
import urllib
from collections import deque
import gettext

targetDir = r"G:\demo01"

def destFile(path):
    if not os.path.isdir(targetDir):
        os.mkdir(targetDir)
    pos = path.rindex('/')
    t = os.path.join(targetDir,path[pos+1:])
    return t

def getQueue(url):
    
    queue =deque()
    urlop = urllib.request.urlopen(url)
    data = urlop.read().decode('UTF-8')    
    linkre = re.compile(r'href="(.+?)" target="_blank" class="pic"')
    for x in linkre.findall(data):
        if 'http' in x:
            queue.append(x)
            print('加入队列-->'+x)
    return queue

def getImg(url,x):
    page = urllib.request.urlopen(url)
    html = page.read().decode('UTF-8')
    reg = r'src="(.+?\.jpg)" alt="'
    imgre = re.compile(reg)
    imglist = re.findall(imgre,html)
    try:
        urllib.request.urlretrieve(imglist[0],destFile(imglist[0]))
        print('正在抓取第%d张图片'%x)
    except:
        print("抓取第%d张图片时出错！"%x)

queue = getQueue('http://www.tooopen.com/img/88_879.aspx')
x = 1
while queue:
    url = queue.popleft()
    getImg(url, x)
    x +=1
