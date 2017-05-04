# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django.db import models
#from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

##################################

from ouds.utils.consts import MODULE

class Catalog(models.Model):
    module = models.CharField(_(u'所属模块'), max_length = 20, choices = MODULE)
    name = models.CharField(_(u'名称'), max_length = 100) # primary_key = True,
    is_display = models.BooleanField(_(u'是否展示'), default = True)
    post_count = models.PositiveIntegerField(_(u'文章数'), default = 0)
    read_count = models.PositiveIntegerField(_(u'浏览数'), default = 0)
    birth_date = models.DateTimeField(_(u'创建时间'), auto_now_add = True)

    class Meta:
        verbose_name = _(u'类别')
        verbose_name_plural = _(u'类别')
        unique_together = ('module', 'name')
        ordering = ['module']
    
    def __unicode__(self):
        return u'%s - %s' % (_([MODULE[o][1] for o in xrange(MODULE.__len__()) if MODULE[o][0] == self.module][0]), self.name)

    def get_absolute_url(self):
        return "/%s/%s/" % (self.module, self.name)

###########################################

class Tag(models.Model):
    catalog = models.ForeignKey(Catalog, related_name = 'tags', verbose_name = _(u'类别'))
    name = models.CharField(_(u'名称'), max_length = 50) # primary_key = True,
    post_count = models.PositiveIntegerField(_(u'文章数'), default = 0)
    read_count = models.PositiveIntegerField(_(u'浏览数'), default = 0)
    birth_date = models.DateTimeField(_(u'创建时间'), auto_now_add = True)

    class Meta:
        verbose_name = _(u'标签')
        verbose_name_plural = _(u'标签')
        unique_together = ('catalog', 'name')
        ordering = ['-post_count', '-read_count']

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.catalog)

    def get_absolute_url(self):
        return "%s%s/" % (self.catalog.get_absolute_url(), self.name)

##############################################

class TopicPublicManager(models.Manager):
    
    def get_query_set(self):
        return super(TopicPublicManager, self).get_query_set().filter(is_public__exact = True, is_approved__exact = True)

##############################################

from ouds.member.models import Profile

class Topic(models.Model):
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    profile = models.ForeignKey(Profile, verbose_name = _(u'作者'))
    catalog = models.ForeignKey(Catalog, related_name = 'topics', verbose_name = _(u'类别'))
    title = models.CharField(_(u'标题'), max_length = 40)
    icon = models.ImageField(_(u'标志'), upload_to = 'imgs/article', blank = True, help_text = u'可空。若上传标志图，限gif，jpg，png之一。请勿大于20K，否则不上传。')
    description = models.TextField(_(u'描述'))
    comment_count = models.PositiveIntegerField(_(u'评论数'), default = 0)
    birth_date = models.DateTimeField(_(u'创建时间'), auto_now_add = True)
    edit_date = models.DateTimeField(_(u'编辑时间')) # auto_now = True
    is_public = models.BooleanField(_(u'是否公开？'), default = True)
    is_approved = models.BooleanField(_(u'是否核准？'), default = False)
    is_recommended = models.BooleanField(_(u'是否推荐？'), default = False)
    is_focused = models.BooleanField(_(u'是否聚焦？'), default = False)
    tags = models.ManyToManyField(Tag, related_name = 'topics', verbose_name = _(u'标签'))
    
    objects = models.Manager()
    published = TopicPublicManager()
    
    class Meta:
        verbose_name = _(u'文章主题')
        verbose_name_plural = _(u'文章主题')
        unique_together = ('catalog', 'title')
        ordering = ['-edit_date']

    def __unicode__(self):
        return u'[%s]%s' % (self.catalog, self.title) 

    def get_absolute_url(self):
        return "%s%s/%s/" % (self.catalog.get_absolute_url(), self.birth_date.strftime("%Y/%m/%d"), self.id)
    
    def read_count(self):
        return self.entries.aggregate(models.Sum('read_count'))['read_count__sum']

    def public_entries(self):
        return self.entries.filter(is_public__exact = True).order_by('birth_date')

##############################################

from ouds.utils.consts import INPUT_FORMAT

class Entry(models.Model):
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    topic = models.ForeignKey(Topic, related_name = 'entries', verbose_name = _(u'文章主题'))
    title = models.CharField(_(u'章节主题'), max_length = 40)
    image = models.ImageField(_(u'图片'), upload_to = 'imgs/article', blank = True, help_text = _(u'可空。若上传标志图，限gif，jpg，png之一。请勿大于300K，否则不上传。'))
    input_format = models.CharField(_(u'输入格式'), max_length = 6, choices = INPUT_FORMAT, default = INPUT_FORMAT[0][0])
    body = models.TextField(_(u'正文'))
    birth_date = models.DateTimeField(_(u'创建时间'), auto_now_add = True)
    read_count = models.PositiveIntegerField(_(u'阅读数'), default = 0)
    is_public = models.BooleanField(_(u'是否公开？'), default = True)
    
    class Meta:
        verbose_name = _(u'文章章节')
        verbose_name_plural = _(u'文章章节')
        unique_together = ('topic', 'title')
        ordering = ['-birth_date']

    def __unicode__(self):
        return u'%s(%s)' % (self.title, self.topic) 

    def get_absolute_url(self):
        return "%s%s/" % (self.topic.get_absolute_url(), self.id)
    
    #def body_html(self):
    #    return mark_safe(self.body)
    
#####################################

class Comment(models.Model):
    id = models.CharField(_(u'主键'), primary_key = True, max_length = 40, editable = False)
    topic = models.ForeignKey(Topic, related_name = 'comments', verbose_name = _(u'文章主题'))
    author = models.CharField(_(u'评论人'), max_length = 20, blank = True, help_text = _(u'可匿名。若未签入且留空，则评论显示IP。'))
    email = models.EmailField(_(u'E-Mail'), max_length = 100, blank = True, help_text = _(u'可空。若填则必须有效，否则无提示跳过。'))
    url = models.URLField(_(u'URL'), blank = True, help_text = _(u'可空。若填则必须前加“http://”，可有效访问，否则无提示跳过。'))
    body = models.TextField(_(u'内容'))
    birth_date = models.DateTimeField(_(u'评论时间'), auto_now_add = True)
    ip = models.IPAddressField(_(u'IP'))

    class Meta:
        verbose_name = _(u'评论')
        verbose_name_plural = _(u'评论')
        ordering = ['-birth_date']

    def __unicode__(self):
        return u'%s - %s' % (self.author, self.ip)

    #def get_absolute_url(self):
    #    return "/comment/%s/%s/" % (self.birth_date.strftime("%Y/%m/%d"), self.id)

######################################

from django.contrib.sites.models import Site

class Link(models.Model):
    module = models.CharField(_(u'所属模块'), unique = True, max_length = 20, choices = MODULE, blank = True)
    sites = models.ManyToManyField(Site, related_name = 'links', verbose_name = _(u'站点'))

    class Meta:
        verbose_name = _(u'模块链接')
        verbose_name_plural = _(u'模块链接')
        
    def __unicode__(self):
        if not self.module:
            module_name = u'首页'
        else:
            module_name = [MODULE[o][1] for o in xrange(MODULE.__len__()) if MODULE[o][0] == self.module][0]

        return u'%s' % _(module_name)



