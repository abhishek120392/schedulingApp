# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='time',
            field=models.DateTimeField(),
        ),
    ]