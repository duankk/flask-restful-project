#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 8/31/2019 8:21 PM 
# @Author : Duan Kunkun
# @Site :  
# @File : user.py 
# @Software: PyCharm
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required

from restdemo.model.user import User as UserModel
from restdemo.until import min_length_str



class User(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'password',
        type=min_length_str(5),
        required=True,
        help='password:{error_msg}'
    )
    parser.add_argument(
        'email',
        type=str,
        required=True,
        help='email error'
    )

    def get(self, username):
        user = UserModel.get_by_username(username)
        if user:
            return user.as_dict()
        return {'message': 'not found user'}, 404

    def post(self, username):
        data = User.parser.parse_args()
        user = UserModel.get_by_username(username)
        if user:
            return {
                'message': 'user exits'
            }
        user = UserModel(
            username= username,
            email= data.get('email')
            )
        user.set_password(data.get('password'))
        user.add()
        return user.as_dict(), 201

    def delete(self, username):
        user = UserModel.get_by_username(username)
        if user:
            user.delete()
            return {
                'message': 'had deleted'
            }
        return {"message": "not found user"}, 204

    def put(self, username):
        user = UserModel.get_by_username(username)
        if user:
            data = User.parser.parse_args()
            user.email = data['email']
            user.set_password(data.get('password'))
            user.update()
            return {'message': 'had changed password!'}
        return {"message":"not found user"}, 204


class UserList(Resource):

    @jwt_required()
    def get(self):
        users = UserModel.get_user_list()
        return [user.as_dict() for user in users]