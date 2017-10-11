# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-11 03:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ScienceNews',
            fields=[
                ('id', models.CharField(max_length=36, primary_key=True, serialize=False)),
                ('first_module', models.CharField(default='News', max_length=30)),
                ('second_module', models.CharField(default='Latest News', max_length=30)),
                ('title', models.CharField(max_length=300)),
                ('author', models.CharField(max_length=60, null=True)),
                ('publish_date', models.CharField(max_length=35, null=True)),
                ('content', models.TextField(null=True)),
                ('crawl_date', models.CharField(max_length=35, null=True)),
                ('from_url', models.CharField(max_length=350, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=32)),
                ('pwd', models.CharField(max_length=32)),
            ],
        ),
    ]