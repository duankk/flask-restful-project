#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 9/2/2019 4:06 PM 
# @Author : Duan Kunkun
# @Site :  
# @File : base.py 
# @Software: PyCharm
from restdemo import db


class Base(db.Model):

    __abstract__ = True

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()