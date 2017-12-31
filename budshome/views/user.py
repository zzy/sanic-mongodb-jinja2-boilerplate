#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sanic import Blueprint
from sanic.response import json

from budshome.settings import page
from budshome.databases import motor_obj

user_bp = Blueprint('user/v1', url_prefix='user')

@user_bp.listener('after_server_start')
async def notify_server_started(books_bp, loop):
    global mongo_obj
    mongo_obj = motor_obj.db
    
    print(u'\nbooks_bp successfully installed \n')

@user_bp.listener('before_server_stop')
async def notify_server_stopping(books_bp, loop):
    mongo_obj = None
    del mongo_obj
    
    motor_obj.close
    print('\nClose mongodb client ... \n')
    
    print('\nbooks_bp successfully uninstalled\n')

@user_bp.route("/sign-in", methods=['POST'])
async def sign_in(request):
    form = request.form
    name_email = form.get('name_email', '').strip()
    password = form.get('password', '').strip()

    user = await mongo_obj.users.find({}, {'title':1, 'stars':1})
    
    return page('user/user.html',
                active_page = "/user/sign-in",
                user = user
    )

@user_bp.route("/register", methods=['POST'])
async def register(request):
    form = request.form
    email = form.get('email', '').strip()
    name = form.get('name', '').strip()
    password = form.get('password', '').strip()
    # password2 = form.get('password2', '').strip()
    invitation_code = form.get('invitation_code', '').strip()

    userIsExist = await mongo_obj.users.find_one({'$or': [{'email': email}, {'name': name}]})
    result = 0
    if userIsExist is None:
        import datetime
        ctime = datetime.datetime.now()

        user = {
            'email': email, 
            'name':name, 
            'password':password, 
            'invitation_code': invitation_code, 
            'ctime': ctime
        }
        await mongo_obj.users.insert_one(user)
    else:
        result = 1
        
    return json({
        "result": result
    })


