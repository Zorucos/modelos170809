# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apli', '0004_auto_20170828_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='statut',
            field=models.CharField(choices=[('modell', 'Modelo'), ('Photograph', 'Fotografo'), ('mMake Up', 'Make Up'), ('Styling', 'Styling'), ('Rrhh', 'Recursos Humanos'), ('verschieden', 'Otro')], default='Modell', max_length=9),
        ),
    ]
