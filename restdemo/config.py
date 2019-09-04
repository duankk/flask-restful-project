#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 9/1/2019 5:17 PM 
# @Author : Duan Kunkun
# @Site :  
# @File : config.py 
# @Software: PyCharm
from datetime import timedelta
import os

class Config:
    # SQLALCHEMY_DATABASE_URI = 'mysql://root:123456@localhost:3306/oms?charset=utf8'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)
    SECRET_KEY = os.environ.get('SECRET_KEY', 'flask123')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlte:///:memory:'

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


app_config={
    'testing': TestingConfig,
    'development': DevelopmentConfig,
    'production': ProductionConfig
}


# 这段话是有问题的
# 哈哈哈
# 我是客户端
# 我今天再次进行更新
