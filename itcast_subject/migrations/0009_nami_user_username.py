# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-26 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itcast_subject', '0008_auto_20160817_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='nami_user',
            name='username',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
