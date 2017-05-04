# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django.contrib import admin

from ouds.article.models import Catalog, Tag, Topic, Entry, Comment, Link

class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name', 'module', 'is_display', 'post_count', 'read_count', 'birth_date')
    list_filter = ('is_display', 'module',)
    search_fields = ('name', 'birth_date')

admin.site.register(Catalog, CatalogAdmin)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'catalog', 'post_count', 'read_count', 'birth_date')
    list_filter = ('catalog',)
    search_fields = ('name', 'catalog__name', 'birth_date')

admin.site.register(Tag, TagAdmin)

class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'catalog', 'is_public', 'is_approved', 'is_recommended', 'is_focused', 'birth_date', 'edit_date')
    search_fields = ('title', 'catalog__name', 'description', 'birth_date', 'edit_date')
    list_filter = ('is_approved', 'catalog')
    filter_horizontal = ('tags',)

admin.site.register(Topic, TopicAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'topic', 'is_public', 'read_count', 'birth_date')
    search_fields = ('title', 'topic__title', 'body')
    list_filter = ('is_public',)

admin.site.register(Entry, EntryAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('topic', 'email', 'author', 'birth_date', 'url', 'ip')
    search_fields = ('topic__title', 'author', 'body', 'email', 'birth_date', 'url', 'ip')

admin.site.register(Comment, CommentAdmin)

class LinkAdmin(admin.ModelAdmin):
    filter_horizontal = ('sites',)

admin.site.register(Link, LinkAdmin)


