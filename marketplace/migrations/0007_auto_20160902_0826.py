# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-02 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0006_auto_20160901_0955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sasviewmodel',
            name='upload_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Date Published'),
        ),
    ]
