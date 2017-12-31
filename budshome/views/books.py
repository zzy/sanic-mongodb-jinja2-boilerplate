#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sanic import Blueprint
from sanic.response import redirect

from budshome.settings import page, ENGINE_PRIORITY
from budshome.utils import chinese_contain_check
from budshome.databases import motor_obj

books_bp = Blueprint('books/v1', url_prefix='books')

@books_bp.listener('after_server_start')
async def notify_server_started(books_bp, loop):
    global mongo_obj
    mongo_obj = motor_obj.db
    
    print(u'\nbooks_bp successfully installed \n')

@books_bp.listener('before_server_stop')
async def notify_server_stopping(books_bp, loop):
    mongo_obj = None
    del mongo_obj
    
    motor_obj.close
    print('\nClose mongodb client ... \n')
    
    print('\nbooks_bp successfully uninstalled\n')

@books_bp.route("/seek")
async def seek(request):
    import time
    begin = time.time()
    
    keyword = request.args.get('kw', '').strip()
    if not keyword:
        return redirect('/books/search')
    
    is_contain_chinese = chinese_contain_check(keyword)
    
    book_name = f'{keyword} 小说 阅读 最新'
    
    
    
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

@books_bp.route("/original")
async def original(request):
    books_original = await mongo_obj.books.find({'is_original': True}, {'title': 1, 'visits': 1}).sort([('visits', -1)]).to_list(length=10)
    
    return page('books/original.html', 
                active_page = "/books/original", 
                books_original = books_original
    )

@books_bp.route("/search")
async def search(request):
    books_search = await mongo_obj.books.find({}, {'title': 1, 'searches': 1}).sort([('searches', -1)]).to_list(length=10)
    
    return page('books/search.html',
                active_page = "/books/search",
                books_search = books_search
    )

@books_bp.route("/stars")
async def stars(request):
    books_stars = await mongo_obj.books.find({}, {'title': 1, 'stars': 1}).sort([('stars', -1)]).to_list(length=10)
    
    return page('books/stars.html',
                active_page = "/books/stars",
                books_stars = books_stars
    )

@books_bp.route("/visits")
async def visits(request):
    books_visits = await mongo_obj.books.find({}, {'title': 1, 'visits': 1}).sort([('visits', -1)]).to_list(length=10)
    
    return page('books/visits.html',
                active_page = "/books/visits",
                books_visits = books_visits
    )

@books_bp.route("/children")
async def children(request):
    books_children = await mongo_obj.books.find({'gender': -1}, {'title': 1, 'visits': 1}).sort([('visits', -1)]).to_list(length=10)
    
    return page('books/children.html',
                active_page = "/books/children",
                books_children = books_children
    )

@books_bp.route("/lady")
async def lady(request):
    books_lady = await mongo_obj.books.find({'gender': 0}, {'title': 1, 'visits': 1}).sort([('visits', -1)]).to_list(length=10)
    
    return page('books/lady.html',
                active_page = "/books/lady",
                books_lady = books_lady
    )

@books_bp.route("/man")
async def man(request):
    books_man = await mongo_obj.books.find({'gender': 1}, {'title': 1, 'visits': 1}).sort([('visits', -1)]).to_list(length=10)
    
    return page('books/man.html',
                active_page = "/books/man",
                books_man = books_man
    )

@books_bp.route("/<book_id>")
async def book_info(request, book_id):
    from bson.objectid import ObjectId
    book = await mongo_obj.books.find_one({'_id': ObjectId(book_id)})
    
    return page('books/book-info.html',
                active_page = "/book/id",
                book = book
    )



