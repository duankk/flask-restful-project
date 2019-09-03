#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# @Time : 9/2/2019 3:03 PM 
# @Author : Duan Kunkun
# @Site :  
# @File : tweet.py 
# @Software: PyCharm
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity

from restdemo.model.tweet import Tweet as TweetModel
from restdemo.model.user import User

class Tweet(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument(
        'body', type=str, required=True,help='required body'
        )

    @jwt_required()
    def post(self, username):
        if current_identity.username != username:
            return {"message":"pls use right token"}
        data = Tweet.parser.parse_args()
        user = User.get_by_username(username)
        if not user:
            return {
                "message": 'not found user'
            }, 404
        tweet = TweetModel(
            user_id=user.id,
            body = data['body']
        )
        tweet.add()
        return {"message": "add tweet is succeed"}

    @jwt_required()
    def get(self, username):
        user = User.get_by_username(username)
        if not user:
            return {
                "message": 'not found user'
            }, 404
        return [t.as_dict() for t in user.tweet]