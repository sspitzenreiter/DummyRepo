# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-11-10 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ujian_aplikasi_1174035', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=70, unique=True),
        ),
    ]
