# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-03 18:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0008_auto_20160303_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='role',
            field=models.CharField(blank=True, choices=[('a', 'President'), ('b', 'Vice President'), ('c', 'Secretary'), ('e', 'Tech Leader'), ('g', 'Treasurer'), ('h', 'Media Manager'), ('n', 'Admin'), ('', 'Member')], default='', max_length=1),
        ),
    ]
