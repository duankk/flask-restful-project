#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 8/31/2019 8:20 PM 
# @Author : Duan Kunkun
# @Site :  
# @File : __init__.py.py 
# @Software: PyCharm
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt import JWT

db = SQLAlchemy()

from .model.user import User as UserModel
from .model.tweet import Tweet
from .resource.user import User, UserList
from .resource.tweet import Tweet
from restdemo.config import app_config


jwt = JWT(None, UserModel.authenticate, UserModel.identify)

def create_app(config_name='development'):
    app = Flask(__name__)
    api = Api(app)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    migrate = Migrate(app, db)
    jwt.init_app(app)

    api.add_resource(UserList, '/users')
    api.add_resource(User, '/user/<string:username>')
    api.add_resource(Tweet, '/tweet/<string:username>')

    return app