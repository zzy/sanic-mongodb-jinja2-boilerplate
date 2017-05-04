# -*- coding: UTF-8 -*-

#===============================================================================
# Author: 骛之
# Revision: 0.1
# Date: 2008-10-07 21:35
# Description: admin file of member module.
#===============================================================================

from django.contrib import admin

from ouds.member.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    search_fields = ('user__username',)

admin.site.register(Profile, ProfileAdmin)


