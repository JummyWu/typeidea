# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-19 06:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20180118_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='target',
            field=models.CharField(max_length=200, verbose_name='\u8bc4\u8bba\u76ee\u6807'),
        ),
    ]
