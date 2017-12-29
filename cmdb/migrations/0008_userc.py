# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-29 01:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0007_auto_20171229_0117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userc',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=60)),
                ('userPass', models.CharField(max_length=60)),
                ('registerDate', models.DateTimeField(default=django.utils.timezone.now, verbose_name='注册日期')),
            ],
        ),
    ]
