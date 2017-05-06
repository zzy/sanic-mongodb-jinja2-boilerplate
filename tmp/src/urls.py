# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@LoSpring.com
# File Name: ouds/settings.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    (r'^lang/', include('django.conf.urls.i18n')),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^admin/', include(admin.site.urls)),
#    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        
    (r'^$', 'ouds.home'),
    (r'^member/', include('ouds.member.urls')),
    (r'^', include('ouds.article.urls')),
)
