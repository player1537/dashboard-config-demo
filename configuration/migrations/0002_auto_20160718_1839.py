# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 18:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='configuration',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='configuration.Configuration'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='configuration',
            name='instrument',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configurations', to='configuration.Instrument'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instruments', to='configuration.Facility'),
        ),
    ]
