# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from data.models import Book, WavFile, Language

admin.site.register(Book)
admin.site.register(Language)
admin.site.register(WavFile)
