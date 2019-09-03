#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 9/2/2019 5:34 PM 
# @Author : Duan Kunkun
# @Site :  
# @File : wsgi.py 
# @Software: PyCharm
import os
import sys

sys.path.insert(0, os.getcwd())

from restdemo import create_app

application = create_app(config_name='production')