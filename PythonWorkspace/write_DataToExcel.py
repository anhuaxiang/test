'''
Created on 2016年11月28日

@author: yanrujing
'''
from xlutils.copy import copy
import os
from xlrd import open_workbook

excel = r'G:\hello.xlsx'
rb = open_workbook(excel)
wb = copy(rb)
sheet = wb.get_sheet(0)

sheet.write(3,0,"小王")
sheet.write(3,1,24)
sheet.write(3,2,12)

os.remove(excel)
wb.save(excel)








