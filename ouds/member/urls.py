# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/auth/urls.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: urls file of auth module.
#===============================================================================

from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

urlpatterns = patterns('ouds.member.views',
        (r'^captcha.png$', 'image'),

        url(r'^register/$', 'register', name='register'),
        url(r'^register/done/$', direct_to_template, {'template': 'member/register_done.ouds', 'extra_context': {'module': None,},}, name = 'register_done'),
        url(r'^activate/(\w+)/$', 'activate', name='activate'),
        url(r'^sign_in/$', 'sign_in', name='sign_in'),
        url(r'^sign_out/$', 'sign_out', name='sign_out'),
        url(r'^([\w\.]+)/$', 'my_zone', name='my_zone'),
        url(r'^([\w\.]+)/(\d+)/$', 'my_zone', name='my_zone_page'),
        url(r'^password/change/$', auth_views.password_change, name='password_change'),
        url(r'^password/change/done/$', auth_views.password_change_done, name='password_change_done'),
        url(r'^password/reset/$', auth_views.password_reset, name='password_reset'),
        url(r'^password/reset/done/$', auth_views.password_reset_done, name='password_reset_done'),
       )
