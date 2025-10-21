import pymysql

conn=pymysql.connect(
    host='localhost',
    # mysql 서버 주소 (localhost:현재 pc)
    user='root',
    # mysql 사용자명 (root:디폴트)
# port= / 기본과 다른 port 사용 시 변경 필요
    password='1234',
    database='exampledb',
    charset='utf8mb4',
    # utf-8 확장 버전
    cursorclass=pymysql.cursors.DictCursor
    # sql 구문 실행 시 결과를 딕셔너리 형태로 반환
)
# mysql서버에 연결하는 함수

cursor=conn.cursor()
# 커서 생성 (명령어 작성 가능)

cursor.execute('SELECT DATABASE()')
# 명령어 실행
print('현재 데이터베이스:',cursor.fetchone())
# cursor.fetchone : 한 번 호출에 한 row 불러옴 / fetchall / fetchmany(int)

conn.close()
# 연결해제함수