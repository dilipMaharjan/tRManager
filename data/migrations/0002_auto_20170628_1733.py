# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 17:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Book',
        ),
        migrations.RenameModel(
            old_name='Languages',
            new_name='Language',
        ),
        migrations.RenameModel(
            old_name='WavFiles',
            new_name='WavFile',
        ),
    ]