# -*- coding: UTF-8 -*-

# Author: 张骛之
# File Name: company/urls.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: urls of trade module

from django import forms
from django.utils.translation import ugettext_lazy as _

from ouds.member.widgets import CaptchaWidget
from ouds.article.models import Topic, Entry, Comment

##############################

class TopicForm(forms.ModelForm):
    tags = forms.CharField(label = _(u'标签'), max_length = 100, widget = forms.TextInput(attrs = {'size': 100}), help_text = u' * 标签间以空格分隔。')
    class Meta:
        model = Topic
        fields = ['title', 'icon', 'catalog', 'is_public', 'description']
        widgets = {
            'title': forms.TextInput(attrs = {'size': 100}),
            'description': forms.Textarea(attrs = {'cols': 80, 'rows': 10}),
        }
    
    def clean(self):    
        if 'title' in self.cleaned_data and 'catalog' in self.cleaned_data:
            if Topic.objects.filter(catalog__exact = self.cleaned_data['catalog'], title__exact = self.cleaned_data['title']):
                raise forms.ValidationError(_(u'“' + self.cleaned_data['catalog'].name + u'”类别中此主题已经存在。'))
        return self.cleaned_data
    
############################

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'is_public', 'image', 'body']
        widgets = {
            'title': forms.TextInput(attrs = {'size': 100}),
            'body': forms.Textarea(attrs = {'cols': 80, 'rows': 18}),
        }
        
    def clean_title(self):
        if Entry.objects.filter(topic__exact = self.instance.topic, title__exact = self.cleaned_data['title']):
            raise forms.ValidationError(_(u'“' + self.instance.topic.title + u'”主题中此章节已经存在。'))
        return self.cleaned_data['title']

############################

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'email', 'url', 'body']
        widgets = {
                   'body': forms.Textarea(),
                   }




