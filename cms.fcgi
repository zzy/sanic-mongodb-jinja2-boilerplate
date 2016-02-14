#! /home/ouds/bin/python
# -*-coding:UTF-8-*-#

import sys

sys.path += ['/home/ouds/lib/python2.6/site-packages/django']
sys.path += ['/home/ouds/Ouds/blog']

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'ouds.settings'

from fcgi import WSGIServer
from django.core.handlers.wsgi import WSGIHandler

WSGIServer(WSGIHandler()).run()
