# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Meeting, Invite

# Register your models here.

admin.site.register(Meeting)
admin.site.register(Invite)