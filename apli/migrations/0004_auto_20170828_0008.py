# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-27 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apli', '0003_auto_20170827_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='statut',
            field=models.CharField(choices=[('modell', 'Modelo'), ('Photograph', 'Fotografo'), ('mMake Up', 'Make Up'), ('Styling', 'Styling'), ('Rrhh', 'Recursos Humanos'), ('verschieden', 'Otro')], default='Modell', max_length=3),
        ),
        migrations.AlterField(
            model_name='project',
            name='sort',
            field=models.CharField(choices=[('Angebot', 'angebot'), ('auftrag', 'aufttrag'), ('Job', 'job')], default='Angebot', max_length=8),
        ),
        migrations.AlterField(
            model_name='project',
            name='statut',
            field=models.CharField(choices=[('Project', 'project'), ('Bestätigung', 'confirmed'), ('Fertig', 'realized'), ('bezhal', 'acquitted'), ('Absagen', 'canceled')], default='Project', max_length=9),
        ),
    ]
