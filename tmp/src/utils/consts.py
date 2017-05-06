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
    ('female', '女'),
    ('male', '男'),
    ('secrecy', '保密'),
)

USER_AREA = (
    ('cn', '中国大陆'),
    ('tw', '中国台湾'),
    ('hk', '中国香港'),
    ('mc', '中国澳门'),
    ('us', '美国'),
)

MESSAGE_FOLDER = (
    (0, '收件箱'),
    (1, '发件箱'),
    (2, '垃圾箱'),
    (3, '档案室'),
)

MESSAGE_TYPE = (
    (0, '公告声明'),
    (1, '联盟消息'),
    (2, '私人联系'),
    (3, '侠客报告'),
)

MESSAGE_STATUS = (
    (0, '未读'),
    (1, '未读删除'),
    (2, '已读'),
    (3, '已读回复'),
    (4, '已读删除'),
)

MODULE = (
    #(u'ready', u'备孕男女'),
    ('she-he', '她和他'),
    ('pregnant', '孕期父母'),
    ('baby', '婴幼养育'),
    ('children', '儿童少年'),
    ('young', '中青年保健'),
    ('elder', '老人社区'),
    #(u'mind', u'心理园地'),
    ('diet', '日常饮食'),
    #(u'vegetarian', u'素食主义'),
    #(u'sport', u'美身运动'),
    ('health', '美容养生'),
    ('fashion', '时尚资讯'),
    ('mall', '叮咚商城'),
)

INPUT_FORMAT = (
    ('editor', '编辑器'),
    ('x-html', '(X)HTML'),
)

IMG_TYPE = ['gif', 'jpg', 'png']
from ouds.settings import MEDIA_ROOT
MARK_IMG = MEDIA_ROOT + '/imgs/ddq.png'
AI_DIR = MEDIA_ROOT + '/imgs/article/'
PADDING = 5
