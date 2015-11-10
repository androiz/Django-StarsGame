# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StarGameApp', '0008_auto_20150319_1323'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='zonaX',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='zonaY',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
