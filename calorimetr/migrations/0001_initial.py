# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-22 19:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('calorie', models.IntegerField(default=0)),
                ('fat', models.IntegerField(default=0)),
                ('carbohydrates', models.IntegerField(default=0)),
                ('protein', models.IntegerField(default=0)),
                ('portion', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Eating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('calorie_num', models.IntegerField(default=0)),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calorimetr.Dish')),
            ],
        ),
    ]