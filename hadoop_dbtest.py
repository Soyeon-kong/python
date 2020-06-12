import pymysql

def select_all():
    conn = pymysql.connect(
        user='root',
        passwd='1234',
        host='localhost',
        port=3708,
        db='virus',
        charset='utf8'
    )
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    #sql = "SELECT * FROM counttable"
    sql = "select * from counttable where countint >= 10 order by countint  desc limit 10"
    cursor.execute(sql, )
    conn.commit()
    return cursor.fetchall()

def connetion(self) :
    conn = pymysql.connect(
        user='root',
        passwd='1234',
        host='localhost',
        port=3708,
        db='travelPlan',
        charset='utf8'
    )
    return conn

if __name__ == '__main__':
    all = select_all()
    for data in all:
        print(data)

    print(select_all())