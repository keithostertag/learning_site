# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 17:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170917_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='step',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='step',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
    ]
