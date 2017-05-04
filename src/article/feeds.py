# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# File Name: gd/member/admin.py
# Revision: 0.1
# Date: 2007-2-5 19:15
# Description: 
#===============================================================================

from django.contrib.syndication.feeds import Feed
from django.utils.feedgenerator import Atom1Feed
from ouds.blog.models import Entry


class RssSiteNewsFeed(Feed):
    title_template = 'feeds/title.html'
    description_template = 'feeds/description.html'
    title = "Border's Log"
    link = '/'
    description = "Simple is powerful"

    def items(self):
        return Entry.published.order_by('-pub_date')[:25]

    def item_pubdate(self, item):
        """
        Takes an item, as returned by items(), and returns the item's
        pubdate.
        """
        return item.pub_date


    item_copyright = 'Copyright (c) 2008, Jiang Bian' # Hard-coded copyright notice.

    item_author_name = "Border"
    item_author_email = "borderj@gmail.com"
    item_author_link = "http://www.b0rder.com"

class AtomSiteNewsFeed(RssSiteNewsFeed):
    feed_type = Atom1Feed
    subtitle = RssSiteNewsFeed.description

