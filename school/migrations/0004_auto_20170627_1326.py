# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-06-27 13:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0003_auto_20170627_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='first_name',
            new_name='first_Name',
        ),
    ]
