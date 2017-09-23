# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('xena', '0006_view_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='Org_query',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('org_query', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='tag',
            name='org_tag',
        ),
        migrations.AddField(
            model_name='organisation',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.AddField(
            model_name='org_query',
            name='org_name',
            field=models.ForeignKey(to='xena.Organisation'),
        ),
    ]
