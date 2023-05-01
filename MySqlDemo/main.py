import pymysql as mysql


def connect_mysql():
    db = mysql.connect(host='localhost', user='root', password='abc123', db='zhenzhizhuojian', port=3306,
                       charset='utf8')
    return db.cursor()


def execute_sql(cursor, sql):
    cursor.execute(sql)
    return cursor.fetchall()


if __name__ == '__main__':
    cursor = connect_mysql()
    sql = 'select * from medicine m where m.medicine_id < 10'
    res = execute_sql(cursor, sql)
    print(res)
