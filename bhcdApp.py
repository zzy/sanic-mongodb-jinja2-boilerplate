#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sanic import Sanic
from sanic_jinja2 import SanicJinja2

app = Sanic(__name__)
app.static('/static', './static')

jinja = SanicJinja2(app)

@app.route('/')
async def index(request):
    return jinja.render('index.html', request, greetings='BudsHome.com will be coming soon ...')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
