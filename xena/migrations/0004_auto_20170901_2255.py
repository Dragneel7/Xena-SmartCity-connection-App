# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 22:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xena', '0003_auto_20170815_0643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=100)),
                ('org_desc', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=50)),
                ('org_tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='xena.Organisation')),
            ],
        ),
        migrations.RemoveField(
            model_name='vote',
            name='uservote',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='vote_view',
        ),
        migrations.AddField(
            model_name='view',
            name='comments',
            field=models.ManyToManyField(through='xena.Comment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Vote',
        ),
    ]
