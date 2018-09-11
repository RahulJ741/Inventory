# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from Login.models import *

# Register your models here.
# class RightsAccessAdmin(admin.ModelAdmin):
#     """docstring forRightsAdmin."""
#     model = RightsAccess
    # list_display = ('user','right')
    # search_fields = ('user','right')


admin.site.register(RightsAccess)
admin.site.register(UsersRights)
