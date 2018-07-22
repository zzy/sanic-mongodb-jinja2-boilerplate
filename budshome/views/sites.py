#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sanic import Blueprint
from sanic.response import redirect

from budshome.settings import page 
from budshome.utils import chinese_contain_check
from budshome.databases import motor_obj

sites_bp = Blueprint('sites/v1', url_prefix='books')

@sites_bp.listener('after_server_start')
async def notify_server_started(sites_bp, loop):
    global mongo_obj
    mongo_obj = motor_obj.db
    
    print('\nsites_bp successfully installed \n')

@sites_bp.listener('before_server_stop')
async def notify_server_stopping(sites_bp, loop):
    mongo_obj = None
    del mongo_obj
    
    motor_obj.close
    print('\nClose mongodb client ... \n')
    
    print('\nsites_bp successfully uninstalled\n')

@sites_bp.route("/seek")
async def seek(request):
    import time
    begin = time.time()
    
    keyword = request.args.get('kw', '').strip()
    if not keyword:
        return redirect('/books/search')
    
    is_contain_chinese = chinese_contain_check(keyword)
    
    book_name = f'{keyword} 小说 阅读 最新'
    
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
    
    use_engine = None
    seek_results = None
    
    if is_contain_chinese:
        for engine in ENGINE_PRIORITY.get('chinese'):
            if engine == 'baidu':
                seek_results = ''
                
                if seek_results:
                    break
    else:
        for engine in ENGINE_PRIORITY.get('non-chinese'):
            await mongo_obj.search_records.update_one({'keyword': keyword, 'use_engine': use_engine}, {'$inc': {'count': 1}}, upsert=True)

        
    
    end =  time.time()
    seek_time = '%.2f' % (end - begin)
    return page('books/search.html',
                active_page = "/books/seek",
                seek_results = seek_results,
                seek_time = seek_time
    )

@sites_bp.route("/original")
async def original(request):
    books_original = await mongo_obj.books.find({'is_original': True}, {'title': 1, 'visits': 1}).sort([('visits', -1)]).to_list(length=10)
    
    return page('books/original.html', 
                active_page = "/books/original", 
                books_original = books_original
    )


@sites_bp.route("/<book_id>")
async def book_info(request, book_id):
    from bson.objectid import ObjectId
    book = await mongo_obj.books.find_one({'_id': ObjectId(book_id)})
    
    return page('books/book-info.html',
                active_page = "/book/id",
                book = book
    )



