import urllib.request
import re
from xlutils.copy import copy
import os
from xlrd import open_workbook

url = 'http://www.stats.gov.cn/tjsj/pcsj/rkpc/5rp/html/t0101.htm'
data = urllib.request.urlopen(url).read().decode('GB2312')

restr = r"<tr height=19 style='mso-height-source:userset;height:14.25pt'>(.*?)</tr>"
datare = re.compile(restr,re.S)                                   
datalist = re.findall(datare,data)
del datalist[0]
del datalist[0]
del datalist[0]
del datalist[0]
del datalist[1]
del datalist[6]
del datalist[9]
del datalist[16]
del datalist[22]
del datalist[-1]
del datalist[-6]
del datalist[0]
j = 1
for x in datalist:
    string = "<td height=19 class=xl3123644 style=\'height:14.25pt\'>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>.*?<td class=xl3423644 align=right x:.*?>(.*?)</td>"    
    data_re = re.compile(string,re.S)
    data_more =  datalist = re.findall(data_re,x)
    y=str(data_more)
    y = y.replace('[','')
    y = y.replace(']','')
    y = y.replace('(','')
    y = y.replace(')','')
    y = y.replace("'",'')
    y = y.replace(' ','')
    list_result = y.split(',')
    print(list_result)
    excel = r'G:\hello.xlsx'
    rb = open_workbook(excel)
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    i = 0
    while i<13:
        sheet.write(j,i,list_result[i])
        i = i+1
    os.remove(excel)
    wb.save(excel)
    j = j+1
    
    
    
    
    
    
    
    
    
    
    
    
    
