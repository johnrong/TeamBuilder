# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 14:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamBuilder', '0014_auto_20160526_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('common', 'common'), ('special', 'special')], default=('common', 'common'), max_length=20, null=True),
        ),
    ]