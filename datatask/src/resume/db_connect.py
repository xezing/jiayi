import pymysql
import db_conf
db = pymysql.connect(host=db_conf.host,
                     port=db_conf.port,
                     user=db_conf.user,
                     password=db_conf.password,
                     db=db_conf.db,
                     charset=db_conf.charset,
                     cursorclass=pymysql.cursors.DictCursor)

cursor=db.cursor()
cursor.execute('select * from ap_mac limit 3')
print(cursor.fetchall())
cursor.execute('select * from ap_mac limit 2')
print(cursor.fetchall())
cursor.close()