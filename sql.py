# 导入pymysql模块
import pymysql
#定义数据库连接
host = '数据库地址'
user = '数据库用户'
password = '您的密码'
database = '数据库名'
charset = 'utf8'
# 连接database
def read(sql):
    conn = pymysql.connect(host=host, user=user,password=password,database=database,charset=charset)
# 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
# 执行SQL语句
    cursor.execute(sql)
    run = cursor.fetchone()
# 关闭光标对象
    cursor.close()
# 关闭数据库连接
    conn.close()
    return(run)



def write(sql):
    conn = pymysql.connect(host=host, user=user,password=password,database=database,charset=charset)
# 得到一个可以执行SQL语句的光标对象
    cursor = conn.cursor()
# 执行SQL语句
    cursor.execute(sql)
    conn.commit()
# 关闭光标对象
    cursor.close()
# 关闭数据库连接
    conn.close()


def queries(SQL):
    conn = pymysql.connect(host=host, user=user,password=password,database=database,charset=charset)
    cursor = conn.cursor()
    cursor.execute(SQL)
    ret = cursor.fetchall()
    cursor.close()
    conn.close()
    return(ret)
