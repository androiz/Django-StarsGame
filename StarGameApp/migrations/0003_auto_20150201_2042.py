# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StarGameApp', '0002_auto_20150201_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='race',
            field=models.ForeignKey(to='StarGameApp.Race'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='race',
            field=models.ForeignKey(to='StarGameApp.Race'),
            preserve_default=True,
        ),
    ]
