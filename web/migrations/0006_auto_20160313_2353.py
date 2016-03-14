# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20160311_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_usd',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rand1',
            field=models.PositiveIntegerField(default=web.models.Product.rand_default),
        ),
    ]
