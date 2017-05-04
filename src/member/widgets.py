# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/common/consts.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: constants.
#===============================================================================

from django.forms import Widget
from django.forms.util import flatatt
from django.utils.safestring import mark_safe

class CaptchaWidget(Widget):
    
    def render(self, name, value, attrs = None):
        '''验证码HTML内容'''
        
        attrs = self.build_attrs(attrs, name=name)
        output = [u'<img height="60" src="/member/captcha.png" />']
        output.append(u'<input %s style="text-transform:uppercase" />' % flatatt(attrs))
        
        return mark_safe(u'<br/>'.join(output))  
