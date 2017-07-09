# -*- coding:utf-8 -*-
import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='941126', db='test')
db = conn.cursor(cursor=pymysql.cursors.DictCursor)
sql = 'select * from news where id > %d' % 2
#sql = 'insert into news (name, access_token) VALUES (%s, %s)', [('111', '123123'), ('112', '132434')]
#affect_num = db.executemany("insert into news (name, access_token) VALUES (%s, %s)", [('111', '123123'), ('112', '132434')])
db.execute(sql)
rows = db.fetchall()
conn.commit()
db.close()
conn.close()
new_id = db.lastrowid
print(new_id)
#print(affect_num)
print(rows)
