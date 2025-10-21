import pymysql

conn=pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='exampledb'
)

cursor=conn.cursor()

sql='select * from employees'
cursor.execute(sql)
employees=cursor.fetchall()
for employee in employees:
    print(employee)

conn.close()