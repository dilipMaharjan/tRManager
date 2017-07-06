# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from data.models import Book, Language

admin.site.register(Book)
admin.site.register(Language)
