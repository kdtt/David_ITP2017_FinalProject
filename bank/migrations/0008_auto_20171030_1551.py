# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_auto_20171030_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]
