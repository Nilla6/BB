# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-05-22 14:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20180522_0905'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]