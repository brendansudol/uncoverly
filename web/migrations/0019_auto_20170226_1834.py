# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_seller_visible_product_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='rand',
            field=models.PositiveIntegerField(default=web.models.rand_int),
        ),
        migrations.AlterField(
            model_name='product',
            name='rand1',
            field=models.PositiveIntegerField(default=web.models.rand_int),
        ),
        migrations.AlterField(
            model_name='product',
            name='rand2',
            field=models.PositiveIntegerField(default=web.models.rand_int),
        ),
    ]
