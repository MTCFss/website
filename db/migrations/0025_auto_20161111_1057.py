# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-11 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0024_auto_20161109_2031'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inscription',
            name='dreamspark_key',
        ),
        migrations.AlterField(
            model_name='inscription',
            name='confirmed',
            field=models.BooleanField(default=False, verbose_name='Fees paid'),
        ),
    ]
