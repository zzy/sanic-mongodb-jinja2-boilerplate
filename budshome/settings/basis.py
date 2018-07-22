#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic.response import html
from jinja2 import Environment, PackageLoader, select_autoescape

# sys.path.append(os.path.dirname(os.getcwd()))
# sys.path.append(os.getcwd())

APP_NAME = 'budshome.com'
HOST = ['localhost:5555', '0.0.0.0:5555']
TIMEZONE = 'Asia/Chengdu'

BH = Sanic(APP_NAME)
BH.static('/static', './static')
# session_interface = InMemorySessionInterface()

# jinjia2 start
env = Environment(
    loader = PackageLoader('budshome', '../templates'),
    autoescape = select_autoescape(['html', 'xml', 'json'])
)

def page(tpl, **kwargs):
    template = env.get_template(tpl)
    return html(template.render(kwargs))
# jinjia2 end

# mongodb start
MONGODB = dict(
    HOST='172.17.0.2',
    PORT='',
    DATABASE='budshome',
    USERNAME='',
    PASSWORD=''
)
# mongodb end




