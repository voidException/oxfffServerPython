# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-27 02:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0005_fruit'),
    ]

    operations = [
        migrations.AddField(
            model_name='fruit',
            name='price',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
