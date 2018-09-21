# -*- coding: utf-8 -*-
import pandas
import pymysql

import readConfig


def get_database_data(sql):
    # 加上字符集参数，防止中文乱码
    db_connect = pymysql.connect(
        host=readConfig.ReadConfig().get_db('host'),
        user=readConfig.ReadConfig().get_db('user'),
        password=readConfig.ReadConfig().get_db('password'),
        port=int(readConfig.ReadConfig().get_db('port')),
        charset='utf8'
    )

    # 利用pandas 模块导入mysql数据
    a = pandas.read_sql(sql, db_connect)
    return a
