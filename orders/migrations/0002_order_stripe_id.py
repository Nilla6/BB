# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-24 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_id',
            field=models.CharField(default='NULL', max_length=255),
        ),
    ]
