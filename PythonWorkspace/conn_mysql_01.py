# -*- coding:utf-8 -*- - 
import mysql.connector
conn = mysql.connector.connect(user='root',password='',database='student')
cursor = conn.cursor()

#创建表
# cursor.execute('create table user(id int primary key,name varchar(20))')

#插入数据
cursor.execute('insert into user values(5,"小王")')
cursor.execute('insert into user values(6,"小李")')
conn.commit()

#查询
# cursor.execute('select * from user')
# print(cursor.fetchall()[1])
# print(cursor.fetchall())

cursor.close()
conn.close()

