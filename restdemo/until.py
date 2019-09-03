#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 9/1/2019 6:36 PM 
# @Author : Duan Kunkun
# @Site :  
# @File : until.py 
# @Software: PyCharm

def min_length_str(min_length):
    def validate(s):
        if s is None:
            raise Exception('password required')
        if not isinstance(s, (int, str)):
            raise Exception('password format error')
        s = str(s)
        if len(s) >= min_length:
            return s
        raise Exception("string must be at least %i characters long" % min_length)
    return validate