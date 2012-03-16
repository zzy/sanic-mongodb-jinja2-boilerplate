# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_page

from ouds.settings import HOST_NAME, HOST_URL, ICON_SIZE, IMAGE_SIZE
from ouds.utils.comms import _md5_key
from ouds.article.models import Catalog, Tag, Topic, Entry, Comment

################################################

@cache_page(60 * 30)
def module(request, module, template_name = 'article/module.ouds'):
    
    user = request.user

    #topics = Topic.published.filter(catalog__module__exact = module)[:100]
    
    return render_to_response(
        template_name,
        {
         'user': user,
         'module': module,
         'catalog': None,
         'tag': None,
         
         #'topics': topics,
         },
    )

################################################

@cache_page(60 * 30)
def catalog(request, module, catalog, template_name = 'article/catalog_tag.ouds'):
    
    user = request.user

    catalog = Catalog.objects.get(module__exact = module, name__exact = catalog)
    catalog.read_count += 1
    catalog.save()
    
    #topics = Topic.published.filter(catalog__exact = catalog)[:100]
    
    return render_to_response(
        template_name,
        {
         'user': user,
         'module': module,
         'catalog': catalog.name,
         'tag': None,
         
         #'topics': topics,
         },
    )

################################################

@cache_page(60 * 30)
def tag(request, module, catalog, tag, template_name = 'article/catalog_tag.ouds'):
    
    user = request.user
    
    tag = Tag.objects.get(catalog__name__exact = catalog, name__exact = tag)
    tag.read_count += 1
    tag.save()
    
    #topics = Topic.published.filter(tags__exact = tag)[:100]
    
    return render_to_response(
        template_name,
        {
         'user': user,
         'module': module,
         'catalog': catalog,
         'tag': tag.name,
         
         #'topics': topics,
         },
    )

##################################

from ouds.utils.consts import IMG_TYPE, AI_DIR
from ouds.article.forms import TopicForm

@login_required
def add_topic(request, topic_form = TopicForm, template_name = 'article/add_topic.ouds'):
    """增加文章"""

    user = request.user
    if request.method == "POST":
        data = request.POST
        data['title'] = data['title'].strip()
        now = datetime.datetime.now()
        topic = Topic(id = _md5_key(now, user.username), profile = user.get_profile(), \
                      edit_date = now, is_approved = True) # is_recommended = True
        topic_form = topic_form(data, instance = topic, auto_id = False)
        if topic_form.is_valid():
            topic = topic_form.save()
            if request.FILES:
                icon = request.FILES['icon']
                if icon.size <= ICON_SIZE and (icon.name[-3:] in IMG_TYPE):
                    topic.icon.save(topic.id + icon.name[-4:], icon, save = True)
            # 更新catalog
            catalog = topic.catalog
            catalog.post_count += 1
            catalog.save()
            # 标签处理
            tags = data['tags'].strip().split()
            for tag in tags:
                # 增加tag
                if not Tag.objects.filter(catalog__exact = catalog, name__exact = tag).exists():
                    Tag(catalog = catalog, name = tag).save()
                # 更新tag和topic-tag
                tag = Tag.objects.get(catalog__exact = catalog, name__exact = tag)
                tag.post_count += 1
                tag.save()
                if not topic.tags.filter(name__exact = tag.name).exists():
                    topic.tags.add(tag)

            return HttpResponseRedirect('/member/%s' % user.username)
    else:
        topic_form = topic_form(auto_id = False)
    
    return render_to_response(
        template_name,
        {
         'user': user,
         'module': None,
         
         'topic_form': topic_form,
         },
       )


##################################

from ouds.article.forms import CommentForm

def topic(request, module, catalog, year, month, day, id, template_name = 'article/topic.ouds'):
    
    user = request.user
    
    topic = Topic.objects.get(id__exact = id)
    if request.method == 'POST':
        entry_id = request.POST['entry_id']
    else:
        public_entries = topic.public_entries()
        if public_entries:
            entry_id = public_entries.latest('birth_date').id
        else:
            entry_id = None
    
    try:
        next_topic = topic.get_next_by_edit_date()
    except Topic.DoesNotExist:
        next_topic = None
            
    try:
        previous_topic = topic.get_previous_by_edit_date()
    except Topic.DoesNotExist:
        previous_topic = None

    comments = topic.comments.all()

    return render_to_response(
        template_name,
        {
         'user': user,
         'host_name': HOST_NAME,
         'host_url': HOST_URL,
         'module': module,
         'catalog': catalog,
         
         'topic': topic,
         'entry_id': entry_id,
         'next_topic': next_topic,
         'previous_topic': previous_topic,
         'comments': comments,
         'comment_form': CommentForm(auto_id = False),
         }
        )

##################################

from ouds.article.forms import EntryForm
from ouds.utils.processimg import watermark

@login_required
def add_entry(request, topic_id, entry_form = EntryForm, template_name = 'article/add_entry.ouds'):
    """增加文章章节"""

    user = request.user
    if not Topic.objects.filter(id__exact = topic_id).exists():
        return HttpResponseRedirect('/member/%s' % user.username)
    else:
        topic = Topic.objects.get(id__exact = topic_id)

    if request.method == "POST":
        data = request.POST
        data['title'] = data['title'].strip()
        entry = Entry(id = _md5_key(datetime.datetime.now(), user.username), topic = topic)
        entry_form = entry_form(data, instance = entry, auto_id = False)
        if entry_form.is_valid():
            entry = entry_form.save()
            if request.FILES:
                image = request.FILES['image']
                if image.size <= IMAGE_SIZE and (image.name[-3:] in IMG_TYPE):
                    entry.image.save(entry.id + image.name[-4:], image, save = True)
                    watermark(AI_DIR + entry.id + image.name[-4:]).save(AI_DIR + entry.id + image.name[-4:], quality = 90)

            return HttpResponseRedirect('/member/%s' % user.username)
    else:
        entry_form = entry_form(auto_id = False)
    
    return render_to_response(
        template_name,
        {
         'user': user,
         'module': None,
         
         'entry_form': entry_form,
         },
       )

################################################

import random
from ouds.utils.consts import MODULE

def search(request, template_name = 'article/search.ouds'):
    
    user = request.user
    
    keywords = request.POST['keywords'].strip()
    topics = Topic.published.filter(Q(title__icontains = keywords) | Q(description__icontains = keywords))
    
    return render_to_response(
        template_name,
        {
         'user': user,
         'module': MODULE[random.randint(0, len(MODULE)-1)][0],

         'keywords': keywords,
         'topics': topics,
         },
    )

#######################################

def comment(request, topic_id, comment_form = CommentForm):
    """发表评论"""

    data = request.POST
    topic = Topic.objects.get(id__exact = topic_id)
    comment = Comment(id = _md5_key(datetime.datetime.now(), data['author']), topic = topic, ip = request.META['REMOTE_ADDR'])
    comment_form = comment_form(data, instance = comment, auto_id = False)
    
    if comment_form.is_valid():
        comment.save()
        
        topic.comment_count += 1
        topic.save()
    #else:
    #    comment_form = comment_form(auto_id = False)

    return HttpResponseRedirect(data['topic_url'])


