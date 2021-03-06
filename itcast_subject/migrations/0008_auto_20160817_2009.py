# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itcast_subject', '0007_remove_nami_user_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='nami_user',
            name='email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nami_user',
            name='firstname',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nami_user',
            name='lastname',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nami_user',
            name='login',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nami_user',
            name='type',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
