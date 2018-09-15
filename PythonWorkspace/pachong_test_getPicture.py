'''
Created on 2016年11月23日
 
@author: yanrujing
'''
 
# import urllib.request
# import socket
# import re
# import sys
# import os
#  
# targetDir = r"G:\demo"
#  
# def destFile(path):
#     if not os.path.isdir(targetDir):
#         os.mkdir(targetDir)
#     pos = path.rindex('/')
#     t = os.path.join(targetDir,path[pos+1:])
#     return t
#  
# if __name__ == '__main__':
#     weburl = 'http://www.douban.com'
#     webheaders = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
#     req = urllib.request.Request(url=weburl,headers=webheaders)
#     webpage = urllib.request.urlopen(req)
#     contentByte = webpage.read()
#     contentByte = contentByte.decode('UTF-8')
#     print(contentByte)
#     print('************************************')
#     for link,t in set(re.findall(r'(http:[^s]*?(jpg|png|gif))', str(contentByte))):
#         print(link)
#         try:
#             urllib.request.urlretrieve(link,destFile(link))
#         except:
#             print('失败')

  
import urllib.request
import re

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    reg = r'src="(.+?\.jpg)" alt="'
    imgre = re.compile(reg)
    html = html.decode('UTF-8')
#     print(html)
    imglist = re.findall(imgre,html)
    x = 0
    for imgurl in imglist:
#         print('**********')
#         print(imgurl)  
#         print('**********')
        try:
            urllib.request.urlretrieve(imgurl,'G:\demo\%s.jpg' % x)
            print('正在抓取第%d张图片'%x)
            x=x+1
        except:
            continue

html = getHtml('http://www.tooopen.com/view/990006.html')
getImg(html)

    










