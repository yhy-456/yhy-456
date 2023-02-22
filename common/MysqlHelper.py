import pymysql
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))

#from DBUtils.PooledDB import PooledDB
from dbutils.pooled_db import PooledDB
from common.config.config import Config
from common.Log import MyLog
import pandas as pd




# print(Config.get_value('mysql','test_host'))
#
# con = pymysql.connect(host=Config.get_value('mysql','test_host'),port=int(Config.get_value('mysql','test_port')),user=Config.get_value('mysql','test_user'),password=Config.get_value('mysql','test_pwd'),charset='utf8')
# cur = con.cursor()
# cur.execute('show databases')
# cur.fetchall()
# cur.close()
# con.close()


class MysqlHelper:
    def __init__(self):
        self.conn = MysqlHelper.getmysqlconn(Config.get_value("mysql", 'test_host'),
                                 int(Config.get_value("mysql", 'test_port')),
                                 Config.get_value("mysql", 'test_user'),
                                 Config.get_value("mysql", 'test_pwd'),
                                 Config.get_value("mysql", 'test_db'))

        self.cur = self.conn.cursor()

    # 释放资源
    def dispose(self):
        self.conn.close()
        self.cur.close()

    @staticmethod
    def getmysqlconn(test_host,test_port,test_user,test_pwd,test_db):
        try:
            __pool_conn = PooledDB(creator=pymysql,
                          mincached=0,  #最小空闲数
                          maxcached=3,  #最大空闲数
                          maxshared=5,  #池中共享连接的最大数量。默认为0，即每个连接都是专用的，不可共享(不常用，建议默认)
                          maxconnections=5,  #被允许的最大连接数。默认为0，无最大数量限制。(视情况而定)
                          blocking=True,    #连接数达到最大时，新连接是否可阻塞。默认False，即达到最大连接数时，再取新连接将会报错。(建议True，达到最大连接数时，新连接阻塞，等待连接数减少再连接)
                          maxusage=0,   #连接的最大使用次数。默认0，即无使用次数限制。(建议默认)
                          setsession=None,  #可选的SQL命令列表，可用于准备会话。(例如设置时区)
                          host=test_host,
                          port=test_port,
                          user=test_user,
                          passwd=test_pwd,
                          db=test_db,
                          use_unicode=True,  #True显示str，False显示byte
                          charset='utf8').connection()
        except BaseException as e:
            MyLog.error("数据库连接错误{}".format(e))
            raise
        return __pool_conn

    def select_num(self,sql):
        MyLog.info('执行sql语句：{}'.format(sql))
        num = self.cur.execute(sql)
        MyLog.info('查询结果：{}'.format(num))
        return num

    def select_all(self,sql):
        MyLog.info('执行sql语句：{}'.format(sql))
        self.cur.execute(sql)
        all = self.cur.fetchall()
        MyLog.info('查询结果：{}'.format(all))
        return all

    def select_one(self,sql):
        MyLog.info('执行sql语句：{}'.format(sql))
        self.cur.execute(sql)
        one = self.cur.fetchone()
        MyLog.info('查询结果：{}'.format(one))
        return one

    def insert(self,sql):
        MyLog.info('执行sql语句：{}'.format(sql))
        num = self.cur.execute(sql)
        self.conn.commit()
        MyLog.info('sql语句新增成功：{}'.format(num))
        return num

    def delete(self,sql):
        MyLog.info('执行sql语句：{}'.format(sql))
        num = self.cur.execute(sql)
        self.conn.commit()
        MyLog.info('sql语句删除成功：{}'.format(num))
        return num

    def update(self,sql):
        MyLog.info('执行sql语句：{}'.format(sql))
        num = self.cur.execute(sql)
        self.conn.commit()
        MyLog.info('sql语句更新成功：{}'.format(num))
        return num





if __name__ == "__main__":
    sql = "select id,phone from ums_member where phone=18998919481;"
    m = MysqlHelper()
    #m.select_num(sql)
    print(m.select_one(sql))
    #print(m.select_all())
    m.dispose()


