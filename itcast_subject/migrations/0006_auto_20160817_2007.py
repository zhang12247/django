# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 12:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itcast_subject', '0005_auto_20160817_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nami_user',
            name='email',
        ),
        migrations.RemoveField(
            model_name='nami_user',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='nami_user',
            name='lastname',
        ),
        migrations.RemoveField(
            model_name='nami_user',
            name='type',
        ),
    ]