# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 20:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_domain_unique'),
        ('event', '0003_auto_20161112_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='site',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site'),
            preserve_default=False,
        ),
    ]
