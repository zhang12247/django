# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='nami_user',
            fields=[
                ('uid', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32)),
                ('password', models.CharField(max_length=32)),
                ('Email', models.CharField(max_length=32)),
                ('FirstName', models.CharField(max_length=8)),
                ('LastName', models.CharField(max_length=8)),
            ],
        ),
    ]