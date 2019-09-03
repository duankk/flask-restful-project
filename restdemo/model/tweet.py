#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 9/2/2019 2:33 PM 
# @Author : Duan Kunkun
# @Site :  
# @File : tweet.py 
# @Software: PyCharm
from sqlalchemy import ForeignKey, func

from restdemo import db
from restdemo.model.base import Base

class Tweet(Base):
    __tablename__ = 'tweet'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, ForeignKey('user.id'))
    body = db.Column(db.String(140))
    create_time = db.Column(db.DateTime, server_default=func.now())

    def __repr__(self):
        return "user_id={}, body={}".format(
            self.user_id, self.body
        )

    def as_dict(self):
        t = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        t['create_time'] = t['create_time'].isoformat()
        return t
