import sqlite3
def insert_sql(sql_name, table_name, time, comment_num, focus_num, sign_num):
    conn = sqlite3.connect(sql_name + '.sqlite3')
    curs = conn.cursor()
    try:
        curs.execute('CREATE TABLE %s(日期 varchar (30), 帖子数 int(20000), 粉丝数 int(20000), 签到人数 int (20000))' % (table_name))
    except:
        pass

    exc = "insert into %s values('%s', '%d', '%d','%d')" %(table_name,time, comment_num, focus_num, sign_num)
    curs.execute(exc)
    conn.commit()