'''
Created on 2016年11月22日

@author: yanrujing
'''
import re
import urllib.request
import urllib

from collections import deque

queue = deque()
visited = set()

url = 'http://www.sina.com'

queue.append(url)
count = 0

while queue:
    url = queue.popleft()
    visited |={url}
    print('已经抓取了'+str(count)+'次，正在抓取'+url)
    count+=1
    
    try:
        urlop = urllib.request.urlopen(url,timeout=2)
        if 'html' not in urlop.getheader('Content-Type'):
            continue
        data = urlop.read().decode('UTF-8')
    except:
        continue
    
    linkre = re.compile(r'href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列-->'+x)
    
    
    
    
    
    
    