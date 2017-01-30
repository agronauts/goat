# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 18:43
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('lists', '0003_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='lists.List'),
        ),
    ]