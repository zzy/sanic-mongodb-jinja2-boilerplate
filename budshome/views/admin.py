#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sanic import Blueprint

from budshome.settings import page
from budshome.databases import motor_obj

admin_bp = Blueprint('admin/v1', url_prefix='admin')

@admin_bp.listener('after_server_start')
async def notify_server_started(admin_bp, loop):
    global mongo_obj
    mongo_obj = motor_obj.db
    
    print('\nadmin_bp successfully installed \n')

@admin_bp.listener('before_server_stop')
async def notify_server_stopping(admin_bp, loop):
    mongo_obj = None
    del mongo_obj
    
    motor_obj.close
    print('\nClose mongodb client ... \n')
    
    print('\nadmin_bp successfully uninstalled\n')





