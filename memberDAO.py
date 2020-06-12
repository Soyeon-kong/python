import pymysql

class Dao():

    def select():
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='virus', port=3708)
        try:
            with conn.cursor() as curs:
                sql = "select * from member"
                curs.execute(sql)
                rows = curs.fetchall()
                return rows
        finally:
            conn.close()

    def insert(member):
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='virus', port=3708)
        try:
            with conn.cursor() as curs:
                sql = "insert into member values (%s,%s,%s,%s)"
                curs.execute(sql, member)
                conn.commit()
        finally:
            conn.close()

    def update(id,pw):
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='virus', port=3708)
        try:
            with conn.cursor() as curs:
                sql = "update member set pw= %s where id = %s"
                curs.execute(sql, (pw, id))
                conn.commit()
        finally:
            conn.close()

    def delete(id):
        conn = pymysql.connect(host='localhost', user='root', password='1234', db='virus', port=3708)
        try:
            with conn.cursor() as curs:
                sql = "delete from member where id = %s"
                curs.execute(sql, id)
                conn.commit()
        finally:
            conn.close()