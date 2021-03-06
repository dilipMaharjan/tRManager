# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 19:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path_to_comments', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img_path', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='WavFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_verse', models.IntegerField()),
                ('e_verse', models.IntegerField()),
                ('anthology', models.CharField(max_length=5)),
                ('version', models.CharField(max_length=5)),
                ('chapter', models.IntegerField()),
                ('file_name', models.CharField(max_length=200)),
                ('file_path', models.CharField(max_length=300)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Books')),
                ('lang', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Languages')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.Users'),
        ),
    ]
