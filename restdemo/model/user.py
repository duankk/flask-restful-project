#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 8/31/2019 8:45 PM 
# @Author : Duan Kunkun
# @Site :  
# @File : user.py 
# @Software: PyCharm
from restdemo import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship
from restdemo.model.base import Base


class User(Base):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String())
    email = db.Column(db.String(64))

    tweet = relationship('Tweet')

    # def __init__(self, username, password,email):
    #     self.username = username
    #     self.password = password
    #     self.email = email
    def __repr__(self):
        return '<User %r>' % self.username

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    @staticmethod
    def get_by_username(username):
        return db.session.query(User).filter(
            User.username == username
        ).first()

    @staticmethod
    def get_by_id(user_id):
        return db.session.query(User).filter(
            User.id == user_id
        ).first()

    @staticmethod
    def get_user_list():
        return db.session.query(User).all()

    @staticmethod
    def authenticate(username, password):
        user = User.get_by_username(username)
        if user:
            if user.check_password(password):
                return user

    @staticmethod
    def identify(payload):
        user_id = payload['identity']
        return User.get_by_id(user_id)
