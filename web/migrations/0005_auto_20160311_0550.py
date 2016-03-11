# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20160228_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_awesome',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='product',
            name='is_visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='rand1',
            field=models.PositiveIntegerField(default=699),
        ),
    ]
