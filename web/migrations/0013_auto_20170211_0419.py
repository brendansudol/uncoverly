# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-11 04:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_remove_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='last_synced',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
