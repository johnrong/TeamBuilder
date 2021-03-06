# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 11:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teamBuilder', '0012_auto_20160526_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='commentList',
            field=models.ManyToManyField(blank=True, related_name='profileCommented', to='teamBuilder.Comment'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='description',
            field=models.TextField(default='This is a description'),
        ),
        migrations.AlterField(
            model_name='project',
            name='publisher',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='projectPublished', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='captain',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teamAsCaptain', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='memberList',
            field=models.ManyToManyField(blank=True, related_name='teamAsMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
