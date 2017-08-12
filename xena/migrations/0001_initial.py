# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('view', models.CharField(max_length=200)),
                ('userview', models.ForeignKey(related_name='views', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.BooleanField(default=False)),
                ('uservote', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('vote_view', models.OneToOneField(to='xena.View')),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_view',
            field=models.ForeignKey(to='xena.View'),
        ),
        migrations.AddField(
            model_name='comment',
            name='usercomment',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
