import redis
import sys
import os
sys.path.append(os.path.dirname(sys.path[0]))

from common.config.config import Config
from common.Log import MyLog



class RedisHelper:
    def __init__(self):
        self.conn = RedisHelper.getredisconn(Config.get_value("redis", 'test_host'),
                                             int(Config.get_value("redis", 'test_port')),
                                             Config.get_value("redis", 'test_pwd'),
                                             int(Config.get_value("redis", 'test_db')))
        self.pipe = self.conn.pipeline(transaction=True)

    @staticmethod
    def getredisconn(test_host,test_port,test_pwd,test_db):
        __redis_pool = redis.ConnectionPool(host = test_host,
                                            port = test_port,
                                            password = test_pwd,
                                            db = test_db,
                                            decode_responses = True)

        __redis_conn = redis.Redis(connection_pool=__redis_pool)
        return __redis_conn

    #获取多个key的值，传键：r.get('manager:service:num','oms:orderId20220711')
    def mget(self,*args):

        if len(args) == 0:
            MyLog.info('查询的key为空')
        else:
            MyLog.info('批量查询的key：{}'.format(args))
            self.pipe.mget(args)
            result = self.pipe.execute()
            MyLog.info('批量查询的结果为：{}'.format(result))

    #设置多个键值，传键值的字典：
    # name_dict = {
    #     'test:4': 'Zarten_4',
    #     'test:5': 'Zarten_5'
    # }
    def mset(self,keyvalue_dict):

        if len(keyvalue_dict) == 0:
            MyLog.info('查询的key为空')
        else:
            key_list = []
            value_list = []
            for key,value in keyvalue_dict.items():
                key_list.append(key)
                value_list.append(value)
            MyLog.info('设置的key：{}'.format(key_list))
            MyLog.info('设置的value：{}'.format(value_list))
            self.pipe.mset(keyvalue_dict)
            result = self.pipe.execute()
            MyLog.info('设置结果：{}'.format(result))

    #给已有的键设置新值，并返回原有的值，传键值：r.getset('test:4','123')
    def getset(self,*args):

        if len(args) == 0:
            MyLog.info('设置的key_value为空')
        else:
            MyLog.info('设置的key_value：{}'.format(args))
            self.pipe.getset(args[0],args[1])
            result = self.pipe.execute()
            MyLog.info('原key:{}的值为：{}'.format(args[0],result))


    #删除键值，传键：r.delete('test:4','test:5')
    def delete(self,*args):

        if len(args) == 0:
            MyLog.info('查询的key为空')
        elif len(args) == 1:
            MyLog.info('删除的key：{}'.format(args[0]))
            self.pipe.delete(args[0])
            result = self.pipe.execute()
            MyLog.info('删除的结果为：{}'.format(result))
        else:
            for key in args:
                self.pipe.delete(key)
            MyLog.info('批量删除的key：{}'.format(args))
            result = self.pipe.execute()
            MyLog.info('批量删除的结果为：{}'.format(result))



if __name__ == '__main__':
    pass
    #r = RedisHelper()
    #r.get('manager:service:num','oms:orderId20220711')
    #r.getset('test:4','123')
    #r.delete('test:4')

