# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-26 09:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teamBuilder', '0010_auto_20160525_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=50)),
                ('time', models.DateTimeField()),
                ('marker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='team',
            name='members',
        ),
        migrations.AddField(
            model_name='team',
            name='memberList',
            field=models.ManyToManyField(blank=True, related_name='teamJoin', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='team',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teamEnroll', to='teamBuilder.Project'),
        ),
        migrations.AddField(
            model_name='profile',
            name='commentList',
            field=models.ManyToManyField(blank=True, related_name='comment_profile', to='teamBuilder.Comment'),
        ),
    ]
