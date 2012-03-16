# -*- coding: UTF-8 -*-

# Author: 长弓骛之
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 

from django import template

register = template.Library()

############

@register.inclusion_tag('_base/general.ouds')
def general(user):
    profile = None;
    if user and user.is_active and user.is_authenticated():
        profile = user.get_profile()

    return {
            'profile': profile,
            }

############

from ouds.article.models import Link

@register.inclusion_tag('_base/sites.ouds')
def sites(module):
    '''网站友情链接'''
    
    if not module:
        module = ''
    sites = Link.objects.get(module__exact = module).sites.all()
    
    return {'sites': sites,}

############

from ouds.article.models import Catalog

@register.inclusion_tag('_base/catalogs.ouds')
def catalogs(module):
    '''本菜单下类别'''

    catalogs = Catalog.objects.filter(is_display__exact = True).order_by('-post_count')
    if not module:
        catalogs = catalogs[:12]
    else:
        catalogs = catalogs.filter(module__exact = module)[:12]
    
    return {'catalogs': catalogs,}

############

from ouds.article.models import Tag

@register.inclusion_tag('_base/tags.ouds')
def tags(module, little_module = 1):
    '''标签'''
    
    tags = Tag.objects.filter(catalog__module__exact = module)
    if little_module:
        tags = tags[:200]
    else:
        tags = tags[:400]
    
    return {'tags': tags,}

#####################

from ouds.article.models import Topic

@register.inclusion_tag('_base/recommend.ouds')
def recommend(module):
    '''本菜单下聚焦和推荐文章'''

    focused_topics = Topic.published.filter(is_focused__exact = True)
    recommended_topics = Topic.published.filter(is_recommended__exact = True)
    if not module:
        focused_topics = focused_topics[:6]
        recommended_topics = recommended_topics[:12]
    else:
        focused_topics = focused_topics.filter(catalog__module__exact = module)[:6]
        recommended_topics = recommended_topics.filter(catalog__module__exact = module)[:12]
    
    return {
            'focused_topics': focused_topics,
            'recommended_topics': recommended_topics,
            }

#####################

@register.inclusion_tag('_base/topics.ouds')
def topics(module, catalog, tag, count = 12, little_module = 1, narrow_tdiv = 0):
    '''模块下最新文章列表'''

    topics = Topic.published.filter(catalog__module__exact = module)
    if not module:
        latest_topics = Topic.published.filter(comment_count__gt = 0)[:count]
        popular_topics = Topic.published.order_by('-comment_count')[:count]
    elif module and not catalog:
        latest_topics = topics[:count]
        popular_topics = topics.order_by('-comment_count')[:count]
    elif catalog and not tag:
        latest_topics = topics.filter(catalog__name__exact = catalog)[:count]
        popular_topics = topics.filter(catalog__name__exact = catalog).order_by('-comment_count')[:count]
    elif tag:
        latest_topics = Topic.published.filter(tags__name__exact = tag)[:count]
        popular_topics = Topic.published.filter(tags__name__exact = tag).order_by('-comment_count')[:count]

    return {
            'module': module,
            'little_module': little_module,
            'narrow_tdiv': narrow_tdiv,
            
            'latest_topics': latest_topics,
            'popular_topics': popular_topics,
            }

#####################

from ouds.article.models import Entry

@register.inclusion_tag('article/entry.ouds')
def entry(entry_id):
    '''指定的文章章节'''
    
    entry = Entry.objects.get(id__exact = entry_id)
    entry.read_count += 1
    entry.save()
    
    try:
        next_entry = entry.get_next_by_birth_date(topic = entry.topic)
        #if next_entry not in entry.topic.public_entries():
        #    next_entry = None
    except Entry.DoesNotExist:
        next_entry = None
    
    try:
        previous_entry = entry.get_previous_by_birth_date(topic = entry.topic)
        #if previous_entry not in entry.topic.public_entries():
        #    previous_entry = None
    except Entry.DoesNotExist:
        previous_entry = None

    return {
            'entry_id': entry_id,
            'entry': entry,
            'next_entry': next_entry,
            'previous_entry': previous_entry,
            }
