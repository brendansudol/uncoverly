# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20170108_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='last_synced',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
