# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('xena', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile', models.IntegerField()),
                ('address', models.CharField(max_length=300)),
                ('family_member', models.IntegerField()),
                ('family_children', models.IntegerField()),
                ('userprofile', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
