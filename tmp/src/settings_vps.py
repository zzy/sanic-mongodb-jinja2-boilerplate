# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: ouds/settings.py
# Revision: 0.1
# Date: 2007-2-5 17:48
# Description: settings.
#===============================================================================

DEBUG = False

TEMPLATE_DEBUG = False

ADMINS = (
    #(u'长弓骛之', 'ourunix@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'postgresql_psycopg2',
        'NAME': 'oudsus_ddq',
        'USER': 'oudsus',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

USE_I18N = True

LOCALE_PATHS = (
    '/home/oudsus/Ouds/ddq/locale',
)

LANGUAGES = (
    ('zh-cn', '简体中文'),
    ('zh-tw', '繁體中文'),
    ('en', 'English'),
    ('de', 'Deutsch'),
#    ('fr', u'Français'),
#    ('it', u'Italiano'),
#    ('pt', u'Português'),
#    ('es', u'Español'),
#    ('sv', u'Svenska'),
#    ('ru', u'Русский'),
#    ('jp', u'日本語'),
#    ('ko', u'한국어'),
)

MEDIA_ROOT = '/home/oudsus/Ouds/ddq/media'

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

SECRET_KEY = '%zg$h*ibw9t3by1t#bm58jn2&i*^u8@0nu30ow=jw1u-pe93s)'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.gzip.GZipMiddleware',
#    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
#    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
#    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'ouds.urls'

TEMPLATE_DIRS = (
    '/home/oudsus/Ouds/ddq/templates',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',

    'ouds.utils',
    'ouds.member',
    'ouds.article',
)

#===============================================================================
# extend settings
#===============================================================================

TEMPLATE_STRING_IF_INVALID = 'DingDongQuan.com'
HOST_NAME = '叮咚泉营养健康'
HOST_URL = 'http://DingDongQuan.com'

AUTH_PROFILE_MODULE = 'member.profile'
LOGIN_URL = '/member/sign_in'

FILE_UPLOAD_MAX_MEMORY_SIZE = 300 * 1000
ICON_SIZE = 20 * 1000
IMAGE_SIZE = 300 * 1000

#===============================================================================
# define for active memeber
#===============================================================================

EMAIL_HOST = 'mail.dingdongquan.com'
EMAIL_PORT = '26'
EMAIL_HOST_USER = 'webmaster@dingdongquan.com'
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'webmaster@dingdongquan.com'
ACCOUNT_ACTIVATION_DAYS = 7

# session and cache
SESSION_COOKIE_AGE = 60 * 60 # 1 hour

CACHE_BACKEND = 'locmem:///'
CACHE_MIDDLEWARE_ANONYMOUS_ONLY = True
CACHE_MIDDLEWARE_SECONDS = 60 * 5 # 5 minutes
CACHE_MIDDLEWARE_KEY_PREFIX = 'ouds'

