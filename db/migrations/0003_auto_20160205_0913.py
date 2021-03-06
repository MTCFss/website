# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 09:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20160204_2302'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('event_type', models.CharField(choices=[('con', 'conference'), ('cha', 'challenge'), ('tra', 'training'), ('tlk', 'talk'), ('unk', 'other')], max_length=3)),
                ('is_ours', models.BooleanField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('link', models.URLField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=10)),
                ('session', models.DateField(auto_now_add=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('dreamspark_key', models.BooleanField(default=False)),
                ('member_card', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='member',
            name='confirmed',
        ),
        migrations.RemoveField(
            model_name='member',
            name='course',
        ),
        migrations.RemoveField(
            model_name='member',
            name='dreamspark_key',
        ),
        migrations.RemoveField(
            model_name='member',
            name='member_card',
        ),
        migrations.RemoveField(
            model_name='member',
            name='new',
        ),
        migrations.AddField(
            model_name='inscription',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db.Member'),
        ),
    ]
