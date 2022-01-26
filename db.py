# 모듈을 불러온다. 
import sqlite3
print(sqlite3.version) # 모듈의 버전 2.6.0
print(sqlite3.sqlite_version) # sqlite의 버전

# DB를 생성한다. 
con = sqlite3.connect('simpledb.sqlite')
print(type(con))

# 데이터 삽입
# connection 객체인 con을 이용해서 cursor 객체를 생성함
cursor = con.cursor()

try:
    cursor.execute("create table alarm(day TEXT, hourmin TEXT, subject TEXT, zoomid INTEGER, password INTEGER, sound INTEGER)")
except:
    cursor.execute("use table alarm")
    
cursor.execute("INSERT INTO alarm VALUES('SUN', '12:25','교육학개론', 19230435, 0920, 0)")

cursor.execute('select * from alarm')
cursor.fetchall()