# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-27 04:12
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teamBuilder', '0017_auto_20160527_0407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(verbose_name='publish_time'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='department',
            field=models.CharField(blank=True, default='School of Data and Computer Science', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='grade',
            field=models.CharField(blank=True, default='2013', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='major',
            field=models.CharField(blank=True, default='Software Engineering', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, default='18800000000', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='realname',
            field=models.CharField(blank=True, default='张三', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='school',
            field=models.CharField(blank=True, default='Sun Yat-Sen University', max_length=20),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default='This is a description'),
        ),
        migrations.AlterField(
            model_name='restriction',
            name='department',
            field=models.CharField(blank=True, default='School of Data and Computer Science', max_length=40),
        ),
        migrations.AlterField(
            model_name='restriction',
            name='major',
            field=models.CharField(blank=True, default='Software Engineering', max_length=40),
        ),
        migrations.AlterField(
            model_name='restriction',
            name='max_num',
            field=models.PositiveIntegerField(blank=True, default=10, null=True),
        ),
        migrations.AlterField(
            model_name='restriction',
            name='min_num',
            field=models.PositiveIntegerField(blank=True, default=3, null=True),
        ),
        migrations.AlterField(
            model_name='restriction',
            name='school',
            field=models.CharField(blank=True, default='Sun Yat-Sen University', max_length=40),
        ),
        migrations.AlterField(
            model_name='team',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, default=['tag1', 'tag2', 'tag3'], null=True, size=None),
        ),
    ]