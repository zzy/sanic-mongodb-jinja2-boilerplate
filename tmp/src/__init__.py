# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@LoSpring.com
# File Name: ouds/_init_.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django.template import loader, Context
from django.http import HttpResponse
from django.views.decorators.cache import cache_page

#from ouds.article.models import Topic

@cache_page(60 * 30)
def home(request, template_name = 'home.ouds'):

    user = request.user
    
    # 玩家默认语言
    language = request.META["HTTP_ACCEPT_LANGUAGE"].lower()
    if 'zh-cn' in language:
        language = 'zh-cn'
    elif 'zh-tw' in language:
        language = 'zh-tw'
    else:
        language = language[:2]
    request.session['django_language'] = language
    
    # she-he|pregnant|baby|children|young|elder|diet|health|fashion|mall
    #she-he_topics = Topic.published.filter(catalog__module__exact = 'she-he')[:20]
    #pregnant_topics = Topic.published.filter(catalog__module__exact = 'pregnant')[:20]
    #baby_topics = Topic.published.filter(catalog__module__exact = 'baby')[:20]
    #children_topics = Topic.published.filter(catalog__module__exact = 'children')[:20]
    #young_topics = Topic.published.filter(catalog__module__exact = 'young')[:20]
    #elder_topics = Topic.published.filter(catalog__module__exact = 'elder')[:20]
    #diet_topics = Topic.published.filter(catalog__module__exact = 'diet')[:20]
    #health_topics = Topic.published.filter(catalog__module__exact = 'health')[:20]
    #fashion_topics = Topic.published.filter(catalog__module__exact = 'fashion')[:20]
    #mall_topics = Topic.published.filter(catalog__module__exact = 'mall')[:20]
    #comment_topics = Topic.published.order_by('-comment_count')[:20]

    c = Context({
                 'user': user,
                 'module': None,
                 
                 #'she-he_topics': she-he_topics,
                 #'pregnant_topics': pregnant_topics,
                 #'baby_topics': baby_topics,
                 #'children_topics': children_topics,
                 #'young_topics': young_topics,
                 #'elder_topics': elder_topics,
                 #'diet_topics': diet_topics,
                 #'health_topics': health_topics,
                 #'fashion_topics': fashion_topics,
                 #'mall_topics': mall_topics,
                 #'comment_topics': comment_topics,
                 },)
    
    t = loader.get_template(template_name)
    return HttpResponse(t.render(c))
