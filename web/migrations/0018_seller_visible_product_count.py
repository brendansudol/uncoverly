# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 01:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_imagedetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='visible_product_count',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
