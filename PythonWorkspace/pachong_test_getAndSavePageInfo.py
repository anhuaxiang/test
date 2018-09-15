'''
Created on 2016年11月22日

@author: yanrujing
'''
import urllib.request
import http.cookiejar
 
# head: dict of header
def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener
 
def saveFile(data):
    save_path = 'G:\\temp.out'
    f_obj = open(save_path, 'wb') # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()
    print('写入文件成功，路径为：'+save_path)  
    
oper = makeMyOpener()
uop = oper.open('http://www.sina.com/', timeout = 1000)
data = uop.read()
saveFile(data)