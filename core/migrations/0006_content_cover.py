# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-01 06:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20160829_1757'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]