# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0019_auto_20161103_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscription',
            name='session',
            field=models.CharField(choices=[('2014-2015', '2014-2015'), ('2015-2016', '2015-2016'), ('2016-2017', '2016-2017')], default='2016-2017', max_length=9),
        ),
    ]