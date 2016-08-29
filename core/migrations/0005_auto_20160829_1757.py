# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_basicitem_introduction'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicitem',
            name='html_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='basicitem',
            name='html_favicon',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='basicitem',
            name='html_keywords',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='basicitem',
            name='html_title',
            field=models.TextField(default=''),
        ),
    ]
