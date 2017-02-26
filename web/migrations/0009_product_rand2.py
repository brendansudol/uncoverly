# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_product_last_synced'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rand2',
            field=models.PositiveIntegerField(default=123),
        ),
    ]
