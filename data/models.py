# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class WavFile(models.Model):
    lang = models.IntegerField()
    s_verse = models.IntegerField()
    e_verse = models.IntegerField()
    anthology = models.CharField(max_length=5)
    version = models.CharField(max_length=5)
    chapter = models.IntegerField()
    file_name = models.CharField(max_length=200)
    file_path = models.CharField(max_length=300)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.lang


class Users(models.Model):
    name = models.CharField(max_length=200)
    img_path = models.CharField(max_length=300)

    def __unicode__(self):
        return self.name


class Comments(models.Model):
    path_to_comments = models.CharField(max_length=300)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.user
