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
