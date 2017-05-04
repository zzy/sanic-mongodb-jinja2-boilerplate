# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: ouds/common/comms.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: common files.
#===============================================================================

###########################################

from django.forms.util import ErrorList

class SpanErrorList(ErrorList):
    def __unicode__(self):
        return self.as_spans()
    def as_spans(self):
        if not self: return u''
        return u'<span class="errorlist">%s</span>' % ''.join([u'<span class="error">%s</span>' % e for e in self])

#===============================================================================
# 分页字典
#===============================================================================

from django.core.paginator import Paginator

from ouds.utils.consts import PER_PAGE

def _paginator_dict(objects, num_page = 1, per_page = PER_PAGE):
    '''分页字典'''

    p = Paginator(objects, per_page)
    page = p.page(num_page)
    
    if page.has_previous():
        previous_page = page.previous_page_number()
    else:
        previous_page = 0
        
    if page.has_next():
        next_page = page.next_page_number()
    else:
        next_page = 0
        
    if p.num_pages > 1:
        last_page = p.num_pages
    else:
        last_page = 0
        
    return {
            'list': page.object_list,
            'start_index': page.start_index(),
            'per_page': per_page,
            'end_index': page.end_index(),
            
            'count': p.count,
            'num_pages': p.num_pages,
            'page_range': p.page_range,
            'previous_page': previous_page,
            'num_page': num_page,
            'next_page': next_page,
            'last_page': last_page,
            }

############################

from django.utils.hashcompat import md5_constructor

def _md5_key(now, username = u'Ouds'):
    '''由时间和帐号构造md5_key'''
    
    return md5_constructor("%s%s" % (now, username.encode('utf-8'))).hexdigest()


