# -*- coding:utf-8 -*- - 
import MySQLdb
conn = MySQLdb.connect(user='root',passwd='',db='student')
cursor = conn.cursor()
# cursor.execute("select version()")
# print cursor.fetchone()

cursor.execute('insert into user values(5,"小王"),(6,"小李")')
conn.commit()
cursor.close()
conn.close()