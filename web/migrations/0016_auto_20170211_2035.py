# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 20:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_seller_social'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='image_main',
            new_name='image',
        ),
    ]
