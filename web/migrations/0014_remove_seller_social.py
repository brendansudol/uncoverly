# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 04:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_auto_20170211_0419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='social',
        ),
    ]
