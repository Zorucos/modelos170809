# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-25 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apli', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='statut',
            field=models.CharField(choices=[('project', 'project'), ('confirmed', 'confirmed'), ('realized', 'realized'), ('acquitted', 'acquitted'), ('canceled', 'canceled')], default='angebot', max_length=8),
        ),
        migrations.AddField(
            model_name='project',
            name='total_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
