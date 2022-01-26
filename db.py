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
    # 새로 테이블을 만들어야 하는 경우
    cursor.execute("CREATE table alarm(DAY VARCHAR2(200 BYTE), HOURMIN VARCHAR2(200 BYTE), SUBJECT VARCHAR2(200 BYTE), ZOOMID NUMBER(10,2), ZOOMPW NUMBER(10,2), SOUND NUMBER(10,2))")
except:
    # 그러지 않아도 되는 경우
    pass

cursor.execute("INSERT INTO alarm VALUES ('SUN', '12:25','교육학개론', 19230435, 0920, 0)")

cursor.fetchall()

con.commit()

for row in cursor.execute('SELECT * FROM alarm ORDER BY SOUND'):
    print(row)

con.commit()
con.close()