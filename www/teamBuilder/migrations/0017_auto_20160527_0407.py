# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 04:07
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamBuilder', '0016_auto_20160527_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, default=['tag1', 'tag2', 'tag3'], null=True, size=None),
        ),
    ]
