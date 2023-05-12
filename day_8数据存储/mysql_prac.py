import pymysql

# data = {
#     'id': '20120001',
#     'name': 'Sun',
#     'age': 22
# }
#
db = pymysql.connect(host='localhost', user='root', password='s13522137936', passwd='3306', db='spiders')
cursor = db.cursor()
#
# table = 'students'
# keys = ','.join(data.keys())
# values = ','.join(['%s'] * len(data))
#
# '''建表'''
# # sql = 'CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL ,age INT NOT NULL ,PRIMARY KEY (id))'
# sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE '.format(table=table, keys=keys,
#                                                                                       values=values)
# update = ','.join(["{key}=%s".format(key=key) for key in data])
# sql += update
# try:
#     if cursor.execute(sql, tuple(data.values()) * 2):
#         print('Successful')
#         db.commit()
# except Exception as e:
#     print('Failed')
#     print(e)
#     db.rollback()
# db.close()

'''查询'''
sql = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
except Exception as e:
    print(e)
