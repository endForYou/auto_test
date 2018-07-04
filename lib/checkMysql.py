#coding=utf8
import MySQLdb
from HReConf import dataConfig


class checkMysql(object):
    #创建数据库连接
    def mysqlConnection(self, host=dataConfig.MySQLInFo.MYSQLHOST, user=dataConfig.MySQLInFo.USER,
                        password=dataConfig.MySQLInFo.PASSWORD, port=dataConfig.MySQLInFo.MYSQLPORT,
                        db=dataConfig.MySQLInFo.DATABASE, charset="utf8"):
        try:
            #连接数据库
            self.conn = MySQLdb.connect(host=host, user=user, port=port, passwd=password, db=db, charset=charset)
            #返回数据库连接对象
            return self.conn

        except:
            print "连接数据库失败"
            raise

    #带参数的查询
    def selectWithParam(self, conn, sql, param):
        #conn为数据库连接对象，sql为执行的sql语句，param为sql中的参数
        cursor = conn.cursor()
        cursor.execute(sql, param)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    #不带参数的查询
    def select(self, conn, sql):
        cursor = conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return data

    #增删改查操作
    def duci(self, conn, sql, param):
        cursor = conn.cursor()
        cursor.execute(sql, param)
        cursor.close()
        conn.commit()
        conn.close()

    #一次性插入多条数据的操作
    def insertMany(self, conn, sql, param):
        cursor = conn.cursor()
        cursor.executemany(sql, param)
        cursor.close()
        conn.commit()
        conn.close()


if __name__ == "__main__":
    sql = "select * from bd_user where dd = %s"
    param = ("300000204")
    conn = checkMysql().mysqlConnection()
    data = checkMysql().selectWithParam(conn, sql, param)
    print data







