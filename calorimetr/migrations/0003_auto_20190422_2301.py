# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-22 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calorimetr', '0002_eating_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eating',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
