# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: ouds/member/models.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: models file of auth module.
#===============================================================================

import datetime
import random
import re

from django.conf import settings
from django.db import models
from django.utils.hashcompat import sha_constructor
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

###############################################

from ouds.member import captcha

class Captcha:
    '''验证码'''
    
    def __init__(self, request, *args, **kwargs):
        self.request = request
        
    @staticmethod
    def text():
        return ''.join([random.choice(captcha.LETTERS) for i in range(captcha.LENGTH)])
    
    def get(self):
        return self.request.session.get(captcha.NAME, '')
    
    def destroy(self):
        self.request.session[captcha.NAME] = ''
        
    def create(self):
        self.request.session[captcha.NAME] = self.text()


#######################################################

SHA1_RE = re.compile('^[a-f0-9]{40}$')

class ActivationManager(models.Manager):
    '''帐号激活管理器'''

    def activate_user(self, active_time):
        if SHA1_RE.search(active_time):
            try:
                profile = self.get(active_time = active_time)
            except self.model.DoesNotExist:
                return _(u'此激活码不存在')
            
            if not profile.active_time_expired():
                user = profile.user
                user.is_active = True
                user.save()

                profile.active_time = datetime.datetime.now()
                profile.save()
                
                return profile.user
            
            return _(u'此激活码已过期')
        
        return _(u'此激活码无效')
    
    def create_inactive_user(self, username, email, password):
        
        # save new user
        new_user = User.objects.create_user(username, email, password)
        new_user.is_active = False
        new_user.save()
        
        # save profile
        profile = self.create_profile(new_user)

        # send mail
        self.send_mail(username, email, profile.active_time)

        return profile
    
    def create_profile(self, new_user):
        active_time = sha_constructor(new_user.username.encode('utf-8') + str(datetime.datetime.now())).hexdigest()
        return self.create(user = new_user, active_time = active_time)

    def send_mail(self, username, email, active_time):
        from django.core.mail import send_mail

        expiration_days = settings.ACCOUNT_ACTIVATION_DAYS

        subject = ''.join(render_to_string('member/email_subject.ouds', {'username': username}).splitlines())
        message = render_to_string(
                'member/email_message.ouds',
                {
                    'username': username,
                    'expiration_days': expiration_days,
                    'active_time': active_time,
                   },
                )

        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

    def delete_expired_users(self):
        for profile in self.all():
            if profile.vip_point_expired():
                user = profile.user
                if not user.is_active:
                    user.delete()

#=========================================================
# extend user profile
#=========================================================

from ouds.utils.consts import SEX, USER_AREA

class Profile(models.Model):
    '''用户详细资料'''
    
    user = models.OneToOneField(User, primary_key = True, verbose_name = _(u'帐号'))
    active_time = models.CharField(_(u'有效时间'), max_length = 40)
    is_public = models.BooleanField(_(u'信息公开'))
    sex = models.CharField(_(u'性别'), max_length = 7, choices = SEX)
    photo = models.ImageField(_(u'形象'), upload_to = 'imgs/member/profile', blank = True)
    birthday = models.DateField(_(u'生日'), blank = True, null = True)
    area = models.CharField(_(u'地域'), max_length = 2, choices = USER_AREA)
    phone = models.CharField(_(u'电话'), max_length = 30, blank = True)
    occupation = models.CharField(_(u'职业'), max_length = 50, blank = True)
    website = models.URLField(_(u'网址'), verify_exists = False, blank = True)
    description = models.TextField(_(u'描述'), blank = True)
    recommender = models.CharField(_(u'推荐人'), max_length = 30, blank = True)

    objects = ActivationManager()

    class Meta:
        verbose_name = _(u'用户资料')
        verbose_name_plural = _(u'用户资料')

    def __unicode__(self):
        return u'%s' % self.user#, _([USER_AREA[o][1] for o in xrange(USER_AREA.__len__()) if USER_AREA[o][0] == self.area][0]), self.occupation)
    
    def get_absolute_url(self):
        return "/member/%s/" % self.user

    def active_time_expired(self):
        expiration_date = datetime.timedelta(days = settings.ACCOUNT_ACTIVATION_DAYS)
        return self.user.date_joined + expiration_date <= datetime.datetime.now()


