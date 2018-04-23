# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import KemiBox, Post

# Register your models here.

admin.site.register(KemiBox )
admin.site.register(Post)