# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 11:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itcast_subject', '0003_remove_nami_user_create_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='nami_user',
            name='Email',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]