# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class RightsAccess(models.Model):
    """(RightsAccess stores the set of access user can have)"""
    name = models.CharField(blank=False, max_length=100)
    is_active = models.BooleanField(default=True)

    class Admin:
        list_display = ('name','is_active')
        search_fields = ('name')

    def __unicode__(self):
        return str(self.name)

class UsersRights(models.Model):
    """(UsersRights user and rights mapping)"""
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    right = models.ForeignKey(RightsAccess, on_delete = models.SET_NULL, null=True)


    class Admin:
        list_display = ('user','right')
        search_fields = ('user','right')

    def __unicode__(self):
        return [str(self.user.username), str(self.rights.name)]
