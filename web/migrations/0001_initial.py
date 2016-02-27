# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(primary_key=True, max_length=64, serialize=False)),
                ('title', models.CharField(max_length=1024)),
                ('state', models.CharField(max_length=64)),
                ('price', models.CharField(max_length=32)),
                ('currency', models.CharField(max_length=32)),
                ('category', models.CharField(max_length=512, null=True, blank=True)),
                ('tags', models.CharField(max_length=512, null=True, blank=True)),
                ('materials', models.CharField(max_length=512, null=True, blank=True)),
                ('views', models.PositiveIntegerField(null=True, blank=True)),
                ('favorers', models.PositiveIntegerField(null=True, blank=True)),
                ('image_main', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.CharField(primary_key=True, max_length=64, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('title', models.CharField(max_length=1024, null=True, blank=True)),
                ('icon_url', models.URLField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='seller',
            field=models.ForeignKey(related_name='products', to='web.Seller'),
        ),
    ]
