import pymysql

conn=pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='exampledb'
)

cursor=conn.cursor()

sql1="""
insert into employees(id,name,deptid,managerid)
values(%s,%s,%s,%s);
"""
# %s는 일반적인 python이나 sql 코드가 아닌 pymysql에서만 지원하는 포맷형식
# 뒤에 값을 차례로 넣으면 숫자는 숫자로, 문자는 문자로 처리해줌

cursor.execute(sql1,(8,'kenneth',8,101))
conn.commit()

conn.close()