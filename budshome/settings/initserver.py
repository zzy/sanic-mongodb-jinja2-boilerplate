#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sanic.response import json
from sanic.exceptions import NotFound, ServerError

from budshome.settings import BH, page
from budshome.databases import motor_obj

from budshome.views import books_bp, user_bp, admin_bp

BH.blueprint(books_bp)
BH.blueprint(user_bp)
BH.blueprint(admin_bp)

@BH.listener('before_server_start')
async def before_server_start(BH, loop):
    global mongo_obj
    mongo_obj = motor_obj.db
    
    print('\n' + BH.name + u' server is starting \n')

@BH.listener('after_server_start')
async def notify_server_started(BH, loop):
    print('\n' + BH.name + u' server successfully started \n')

# @BH.middleware('request')
# async def init_session(request):
#     await session_interface.open(request)
# 
# @BH.middleware('response')
# async def save_session(request, response):
#     await session_interface.save(request, response)

@BH.route("/")
async def home(request):
    books_stars = await mongo_obj.books.find({}, {'title':1, 'stars':1}).sort([('stars', -1)]).to_list(length=10)
    books_searches = await mongo_obj.books.find({}, {'title':1, 'searches':1}).sort([('searches', -1)]).to_list(length=10)
    books_visits = await mongo_obj.books.find({}, {'title':1, 'visits':1}).sort([('visits', -1)]).to_list(length=10)
    
    # print("request-"+str(request))
    # print("request.url-"+str(request.url))
    # print("request.args-"+str(request.args))
    # print("request.json-"+str(request.json))
    # print("request.raw_args-"+str(request.raw_args))
    # print("request.files-"+str(request.files))
    # print("request.form-"+str(request.form))
    # print("request.body-"+str(request.body))
    # print("request.ip-"+str(request.ip))
    # print("request.app-"+str(request.app))
    # print("request.scheme-"+str(request.scheme))
    # print("request.host-"+str(request.host))
    # print("request.path-"+str(request.path))
    # print("request.query_string-"+str(request.query_string))
    # print("request.uri_template-"+str(request.uri_template))
    
    return page('home.html',
                active_page = "/",
                books_stars = books_stars,
                books_searches = books_searches,
                books_visits = books_visits
    )

@BH.route("/robots.txt")
async def robots(request):
    from sanic.response import text
    return text('User-agent: * \nCrawl-delay: 10 \nDisallow: /admin')

@BH.exception(NotFound)
async def e404(request, exception):
    await handle_exception(request, exception)

    return page('404.html')

# @BH.exception(RequestTimeout)
# async def e408(request, exception):
#     await handle_exception(request, exception)
#     
#     return json(
#         status = exception.status_code,
#         exception = "{}".format(exception)
#     )

@BH.exception(ServerError)
async def e500(request, exception):
    await handle_exception(request, exception)

    return json(
        status = exception.status_code,
        exception = "{}".format(exception)
    )

@BH.listener('before_server_stop')
async def notify_server_stopping(BH, loop):
    print('\n' + BH.name + u' server will be stopped \n')

@BH.listener('after_server_stop')
async def after_server_stop(BH, loop):
    mongo_obj = None
    del mongo_obj
    
    motor_obj.close
    print('\nClose mongodb client ... \n')
    
    print('\n' + BH.name + u' server successfully stopped \n')

async def handle_exception(request, exception):
    print("\n" + str(exception.status_code) + ": " + request.url + "-" + str(exception) + "\n")
    
    
    