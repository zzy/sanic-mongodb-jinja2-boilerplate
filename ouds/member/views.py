# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Contact: ouds@gaiding.com
# Project: Game
# File Name: ouds/member/views.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: views file of member module.
#===============================================================================

import datetime

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from cStringIO import StringIO
from random import randint, choice

from PIL import Image, ImageDraw, ImageFont

from ouds.member import captcha
from ouds.member.models import Captcha, Profile

def image(request):
    """验证码图片"""
    
    captcha_text = Captcha(request).get()
    response = HttpResponse()
    if captcha_text:
        image = Image.new("RGBA", (captcha.LENGTH * captcha.FONT_SIZE - 26, captcha.FONT_SIZE), (0,0,0,0))
        canvas = ImageDraw.Draw(image)
        
        for i in range(0, len(captcha_text)):
            # font = ImageFont.truetype(choice(captcha.FONTS), captcha.FONT_SIZE)
            # canvas.text((captcha.FONT_SIZE*i+2, -4), captcha_text[i], font = font, fill = choice(captcha.COLOURS))
            horizon = 1; verticality  = -1
            if i>0: horizon = (captcha.FONT_SIZE - 5) * i
            if i%2 == 0: verticality = 2
            canvas.text((horizon, verticality), captcha_text[i], fill = choice(captcha.COLOURS))
            
        out = StringIO()
        image.save(out, "PNG")
        out.seek(0)
        response['Content-Type'] = 'image/png'
        response.write(out.read())
        
    return response

#=====================
# 注册
#=====================

from ouds.member.forms import RegisterForm, SignInForm

def register(request, register_form = RegisterForm, template_name = 'member/register.ouds'):
    """注册帐号"""

    user = request.user;
    if user.is_authenticated():
        return HttpResponseRedirect('/')
    elif request.method == 'POST':
        data = request.POST
        data['captcha_text'] = Captcha(request).get()
        register_form = register_form(data, request.FILES, auto_id = False)
        if register_form.is_valid():
            # 创建未激活用户
            profile = register_form.save()
            # 上传图片
            if request.FILES:
                photo = request.FILES['photo']
                if photo.size < 30 * 1000:
                    profile.photo.save(str(profile.id) + photo.name[-4:], photo, save = True)
            
            return HttpResponseRedirect('/member/register/done')
    else:
        register_form = register_form(auto_id = False)

    Captcha(request).create()

    return render_to_response(
                              template_name,
                              {
                               'user': user,
                               'module': None,
                               
                               'register_form': register_form,},
                              )

#===========================
# 帐号激活、登录、注销
#===========================

from django.contrib.auth import authenticate, login, logout

def activate(request, active_time, template_name = 'member/activate.ouds'):
    """帐号激活"""
    
    activation_result = Profile.objects.activate_user(active_time.lower())
    try:
        profile = Profile.objects.get(user = activation_result)
        user = profile.user
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        login(request, user)
        return HttpResponseRedirect('/')
    except:
        return render_to_response(
                template_name,
                {
                 'user': request.user,
                 'module': None,
                 
                 'activation_result': activation_result,
                 },
               )

#################################################

def sign_in(request, sign_in_form = SignInForm, template_name = 'member/sign_in.ouds'):
    """会员签入"""

    user = request.user;
    if request.method == "POST":
        data = request.POST.copy()
        data['captcha_text'] = Captcha(request).get()
        sign_in_form = sign_in_form(data, auto_id = False)
        if sign_in_form.is_valid():
            user = authenticate(username = data['username'].lower(), password = data['password'])
            if user and user.is_active:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        sign_in_form = sign_in_form(auto_id = False)

    Captcha(request).create()

    return render_to_response(
            template_name,
            {
             'user': user,
             'module': None,
             
             'sign_in_form': sign_in_form,
             },
           )

####################################################

def sign_out(request):
    """全员签退"""

    logout(request)
    return HttpResponseRedirect('/')

####################################################

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from ouds.article.models import Topic
from ouds.utils.comms import _paginator_dict

@login_required
def my_zone(request, username, num_page = 1, template_name = 'member/my_zone.ouds'):
    """我的地盘"""

    user = request.user
    if username == user.username:
        profile = user.get_profile()
    else:
        profile = User.objects.get(username__exact = username).get_profile()

    context_dict = {
                    'user': user,
                    'module': None,
                    
                    'username': username,
                    }
    context_dict.update(_paginator_dict(Topic.objects.filter(profile__exact = profile), int(num_page)))

    return render_to_response(
        template_name,
        context_dict,
       )
