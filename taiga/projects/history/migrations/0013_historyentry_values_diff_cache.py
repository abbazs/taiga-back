# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-11 12:17
from __future__ import unicode_literals

from django.db import migrations
import django_pgjson.fields


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0012_auto_20160629_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='historyentry',
            name='values_diff_cache',
            field=django_pgjson.fields.JsonField(blank=True, default=None, null=True),
        ),
    ]