# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20160227_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='currency',
            field=models.CharField(blank=True, null=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_main',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(blank=True, null=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(blank=True, related_name='products', null=True, to='web.Seller'),
        ),
        migrations.AlterField(
            model_name='product',
            name='state',
            field=models.CharField(blank=True, null=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(blank=True, null=True, max_length=1024),
        ),
    ]
