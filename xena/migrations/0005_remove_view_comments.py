# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 01:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('xena', '0004_auto_20170901_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='view',
            name='comments',
        ),
    ]
