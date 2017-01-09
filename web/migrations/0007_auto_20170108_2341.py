# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20160313_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='seller',
            name='listings_all_count',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='num_favorers',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='social',
            field=jsonfield.fields.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seller',
            name='story',
            field=models.TextField(blank=True, null=True),
        ),
    ]
