# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 09:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teamBuilder', '0007_auto_20160525_0923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='tags',
        ),
    ]
