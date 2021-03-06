# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 07:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apli', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, verbose_name='Title')),
                ('start', models.DateTimeField(verbose_name='Start')),
                ('end', models.DateTimeField(verbose_name='End')),
                ('all_day', models.BooleanField(default=False, verbose_name='All day')),
                ('url', models.CharField(blank=True, max_length=200, verbose_name='Url')),
                ('color', models.CharField(blank=True, max_length=200, verbose_name='Color')),
                ('comment', models.CharField(blank=True, max_length=500)),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('Started', 'Started'), ('Finished', 'Finished')], default='Not Started', max_length=15)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apli.Project')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
