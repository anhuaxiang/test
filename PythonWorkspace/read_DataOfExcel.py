'''
Created on 2016年11月28日

@author: yanrujing
'''
import xlrd
import xlwt
from datetime import date,datetime
 
def read_excel():
    data = xlrd.open_workbook(r'G:\hello.xlsx')
    print(data.sheet_names())
#     通过索引得表
#     table = data.sheets()[0]
#     通过索引顺序得表
#     table = data.sheet_by_index(0)
#     通过表名称得表
    table = data.sheet_by_name(u'Sheet1')
    print(table.name,table.nrows,table.ncols)
    
    print(table.row_values(0))
    print(table.col_values(0))
    print('********************')
    
    for rownum in range(table.nrows):
        print(table.row_values(rownum))
    print('********************')
    print(table.cell(0,0).value)

if __name__ == '__main__':
    read_excel()

