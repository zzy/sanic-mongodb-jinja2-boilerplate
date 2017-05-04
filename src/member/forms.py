# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: forms file of auth module.
#===============================================================================

from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

from ouds.utils.consts import SEX, USER_AREA
from ouds.member.models import Profile
from ouds.member.widgets import CaptchaWidget

class RegisterForm(forms.Form):
    """用户详细资料"""

    captcha = forms.CharField(label = _(u'验证码'), widget = CaptchaWidget(), help_text = u' * 请输入图片上的字符。')
    username = forms.CharField(label = _(u'用户帐号'), max_length = 30, help_text = u' * 任何字符均可')
    #first_name = forms.CharField(label = _(u'姓氏'), max_length = 30, help_text = u' * 用于邮件敬称、游戏公文')
    #last_name = forms.CharField(label = _(u'名字'), max_length = 30, help_text = u' * 用于邮件敬称、游戏公文')
    #type = forms.ChoiceField(label = _(u'游戏类型'), choices = MEMBER_TYPE, help_text = u' * 重要：若更改每城市各建筑会降级一半<br/>武型没有任何限制；文型不受攻击，但无兵部')
    photo = forms.ImageField(label = _(u'个人形象'), required = False, help_text = u'须小于30KB，否则忽略')
    email = forms.EmailField(label = _(u'电子邮箱'), max_length = 75, help_text = u' * 激活帐号所必需')
    #is_email_public = forms.BooleanField(label = _(u'邮箱公开'), required = False, help_text = u' * 是否向其它玩家公开邮箱')
    password = forms.CharField(label = _(u'密钥'), widget = forms.PasswordInput, help_text = u' * 五个字符或以上')
    password_again = forms.CharField(label = _(u'密钥确认'), widget = forms.PasswordInput)
    #sex = forms.ChoiceField(label = _(u'性别'), choices = SEX_TYPE, required = False)
    #birthday = forms.DateField(label = _(u'生日'), required = False, help_text = u'格式如：3/4/02, 2002-3-4, 3/4/2002.<br/>生日会获得奖励，修改需要贡献点。')
    #area = forms.ChoiceField(label = _(u'地域'), choices = USER_AREA)
    #phone = forms.CharField(label = _(u'电话'), max_length = 30, required = False, help_text = u'如果游戏中需要无线服务，请填手机号码')
    #occupation = forms.CharField(label = _(u'职业'), max_length = 50, required = False)
    #website = forms.URLField(label = _(u'网址'), required = False)
    #description = forms.CharField(label = _(u'描述'), widget = forms.Textarea, required = False)
    #recommender = forms.CharField(label = _(u'推荐人'), max_length = 30, required = False, help_text = u'推荐人会受到贡献点和资源双重奖励')
    tos = forms.BooleanField(label=_(u'理解并且同意注册条款'), widget=forms.CheckboxInput)
    
    def clean_tos(self):
        if self.cleaned_data.get('tos', False):
            return self.cleaned_data['tos']
        raise forms.ValidationError(_(u'You must agree to the terms to register'))
    
    def clean_captcha(self):
        if self.cleaned_data['captcha'].upper() == self.data['captcha_text']:
            return self.cleaned_data['captcha']
        else:
            raise forms.ValidationError(_(u'验证码不正确'))
    
    def clean_username(self):
        if len(self.cleaned_data['username']) < 2:
            raise forms.ValidationError(_(u'用户帐号最少需要2个字符。'))
        try:
            User.objects.get(username__iexact = self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_(u'此用户帐号已经被使用。'))

    def clean_email(self):
        if User.objects.filter(email__iexact = self.cleaned_data['email']):
            raise forms.ValidationError(_(u'邮件地址已被使用。'))
        return self.cleaned_data['email']

    def clean(self):
        if 'password' in self.cleaned_data and 'password_again' in self.cleaned_data:
            if len(self.cleaned_data['password']) < 5:
                raise forms.ValidationError(_(u'密码最少需要5位。'))
            if self.cleaned_data['password'] != self.cleaned_data['password_again']:
                raise forms.ValidationError(_(u'两次输入的密码必须相同。'))
        return self.cleaned_data
    
    def save(self):
        return Profile.objects.create_inactive_user(
                # auth_user
                username = self.cleaned_data['username'].lower(),
                #first_name = self.cleaned_data['first_name'],
                #last_name = self.cleaned_data['last_name'],
                #type = self.cleaned_data['type'],
                email = self.cleaned_data['email'],
                password = self.cleaned_data['password'],
                # auth_extendprofile
                #is_email_public = self.cleaned_data['is_email_public'],
                #sex = self.cleaned_data['sex'],
                #birthday = self.cleaned_data['birthday'],
                #area = self.cleaned_data['area'],
                #phone = self.cleaned_data['phone'],
                #occupation = self.cleaned_data['occupation'],
                #website = self.cleaned_data['website'],
                #description = self.cleaned_data['description'],
                #recommender = self.cleaned_data['recommender'],
               )

#############################

class RegisterNoEmail(RegisterForm):
    bad_domains = ['aim.com', 'aol.com', 'email.com', 'gmail.com',
                   'googlemail.com', 'hotmail.com', 'hushmail.com',
                   'msn.com', 'mail.ru', 'mailinator.com', 'live.com']

    def clean_email(self):
        email_domain = self.cleaned_data['email'].split('@')[1]
        if email_domain in self.bad_domains:
            raise forms.ValidationError(_(u'本站拒绝此域邮箱。'))
        return self.cleaned_data['email']

#############################

class SignInForm(forms.Form):
    """用户登录表单"""
    
    captcha = forms.CharField(label = _(u'验证码'), widget = CaptchaWidget(), help_text = u' * 请输入图片上的字符。')
    username = forms.CharField(label = _(u'Username'), max_length = 30)
    password = forms.CharField(label = _(u'Password'), widget = forms.PasswordInput(render_value = False))
    
    def clean_captcha(self):
        if self.cleaned_data['captcha'].upper() == self.data['captcha_text']:
            return self.cleaned_data['captcha']
        else:
            raise forms.ValidationError(_(u'验证码不正确'))

#############################

from ouds.utils.consts import MESSAGE_FOLDER, MESSAGE_TYPE, MESSAGE_STATUS

class MessageForm(forms.Form):
    """消息/报告"""
    
    receiver = forms.CharField(label = _(u'接收人'), max_length = 120, help_text = u'多人接收以\',\'号分隔')
    title = forms.CharField(label = _(u'标题'), max_length = 50, help_text = u'勿超过50字符')
    message = forms.CharField(label = _(u'消息'), widget = forms.Textarea)
    sent_time = forms.CharField(label = _(u'发送时间'), max_length = 20)
    
