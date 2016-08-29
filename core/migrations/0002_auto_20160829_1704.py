# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 17:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicitem',
            name='facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicitem',
            name='google',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='basicitem',
            name='twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
