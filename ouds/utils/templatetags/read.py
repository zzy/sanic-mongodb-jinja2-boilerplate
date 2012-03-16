# -*- coding: UTF-8 -*-

# Author: 张骛之
# Contact: ouds@thinkerunion.net
# File Name: comapny/templatetags.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 

import datetime

from django import template
from django.utils.translation import ugettext_lazy as _

register = template.Library()

###############################

@register.filter
def dict_filter(dict, key):
    '''取得字典中键对应的值'''

    return dict[key]

###############################

@register.filter
def make_tuple(key, value):
    '''组合一个元组'''

    return (key, value)

##############################

@register.filter
def tuple_filter(key, tuple_name):
    '''根据键搜索元组中子元组的值'''

    exec 'from ouds.utils.consts import %s as tuple_name' %tuple_name
    for o in xrange(tuple_name.__len__()):
        if tuple_name[o][0] == key:
            return _(tuple_name[o][1])

##############################

@register.filter
def int2time(seconds, multiple = 1):
    '''转化秒数为时间'''

    time = datetime.timedelta(seconds = seconds * multiple)
    
    return {
            'days': time.days,
            'time': datetime.timedelta(seconds = time.seconds),
           }

##################################

@register.filter
def time2int(time):
    '''转化时间为天、秒数'''
    
    time -= datetime.datetime.now()
    days = time.days; seconds = time.seconds
    if time.days < 0:
        days = 0; seconds = 0
    
    return {
            'days': days,
            'time': seconds,
           }

##################################

@register.filter
def is_lte(a, b):
    
    return a <= b

##################################

@register.filter
def subtract(subtracter, subtracted):
    '''减'''
    
    return subtracted - subtracter

##################################

@register.filter
def multiply(multiplied, multiplier = 0.01):
    '''乘'''
    
    return int(multiplied * multiplier)
