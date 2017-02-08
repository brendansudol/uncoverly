# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_product_rand2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='tw_featured',
            field=models.BooleanField(default=False),
        ),
    ]
