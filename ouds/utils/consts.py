# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: ouds/common/consts.py
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: constants.
#===============================================================================

PER_PAGE = 25 # 分页量

SEX = (
    (u'female', u'女'),
    (u'male', u'男'),
    (u'secrecy', u'保密'),
)

USER_AREA = (
    (u'cn', u'中国大陆'),
    (u'tw', u'中国台湾'),
    (u'hk', u'中国香港'),
    (u'mc', u'中国澳门'),
    (u'us', u'美国'),
)

MESSAGE_FOLDER = (
    (0, u'收件箱'),
    (1, u'发件箱'),
    (2, u'垃圾箱'),
    (3, u'档案室'),
)

MESSAGE_TYPE = (
    (0, u'公告声明'),
    (1, u'联盟消息'),
    (2, u'私人联系'),
    (3, u'侠客报告'),
)

MESSAGE_STATUS = (
    (0, u'未读'),
    (1, u'未读删除'),
    (2, u'已读'),
    (3, u'已读回复'),
    (4, u'已读删除'),
)

MODULE = (
    #(u'ready', u'备孕男女'),
    (u'she-he', u'她和他'),
    (u'pregnant', u'孕期父母'),
    (u'baby', u'婴幼养育'),
    (u'children', u'儿童少年'),
    (u'young', u'中青年保健'),
    (u'elder', u'老人社区'),
    #(u'mind', u'心理园地'),
    (u'diet', u'日常饮食'),
    #(u'vegetarian', u'素食主义'),
    #(u'sport', u'美身运动'),
    (u'health', u'美容养生'),
    (u'fashion', u'时尚资讯'),
    (u'mall', u'叮咚商城'),
)

INPUT_FORMAT = (
    (u'editor', u'编辑器'),
    (u'x-html', u'(X)HTML'),
)

IMG_TYPE = ['gif', 'jpg', 'png']
from ouds.settings import MEDIA_ROOT
MARK_IMG = MEDIA_ROOT + '/imgs/ddq.png'
AI_DIR = MEDIA_ROOT + '/imgs/article/'
PADDING = 5
