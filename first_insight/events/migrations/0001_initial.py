# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 08:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=300)),
                ('link', models.CharField(blank=True, default='', max_length=300)),
                ('img', models.CharField(blank=True, default='', max_length=300)),
                ('author', models.CharField(blank=True, default='', max_length=300)),
                ('datetime', models.CharField(blank=True, default='', max_length=300)),
            ],
        ),
    ]
