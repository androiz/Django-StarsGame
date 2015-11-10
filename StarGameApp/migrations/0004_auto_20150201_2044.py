# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StarGameApp', '0003_auto_20150201_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='race',
            name='name',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='unit',
            name='name',
            field=models.CharField(unique=True, max_length=20),
            preserve_default=True,
        ),
    ]
