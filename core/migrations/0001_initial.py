# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-29 16:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasicItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=256)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('title', models.CharField(default='', max_length=256)),
                ('description', models.TextField(default='')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('position', models.IntegerField(default=0, unique=True)),
                ('span', models.IntegerField(default=3)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('title', models.CharField(default='', max_length=256)),
                ('description', models.TextField(default='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='content', to='core.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ContentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modified_at', models.DateTimeField(auto_created=True, auto_now=True)),
                ('caption', models.CharField(default='', max_length=256)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='core.Content')),
            ],
        ),
    ]
