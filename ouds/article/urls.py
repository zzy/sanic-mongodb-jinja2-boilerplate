# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django.conf.urls.defaults import patterns, url

modules = 'she-he|pregnant|baby|children|young|elder|diet|health|fashion|mall'

urlpatterns = patterns('ouds.article.views',
    url(r'^(' + modules + ')/$', 'module', name = 'module'),
    url(r'^(' + modules + ')/([^/]+)/$', 'catalog', name = 'catalog'),
    url(r'^(' + modules + ')/([^/]+)/([^/]+)/$', 'tag', name = 'tag'),
    url(r'^article/add_topic/$', 'add_topic', name='add_topic'),
    url(r'^(' + modules + ')/([^/]+)/(\d{4})/(\d{2})/(\d{2})/([^/]+)/$', 'topic', name = 'topic'),
    url(r'^article/([^/]+)/add_entry/$', 'add_entry', name='add_entry'),
    #url(r'^(' + modules + ')/([^/]+)/(\d{4})/(\d{2})/(\d{2})/([^/]+)/([^/]+)/$', 'entry', name = 'entry'),
    url(r'^article/search/$', 'search', name = 'search'),
    url(r'^article/([^/]+)/comment/$', 'comment', name='comment'),
)

