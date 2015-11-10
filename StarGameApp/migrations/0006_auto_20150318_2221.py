# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StarGameApp', '0005_building_generaltechnology'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thematic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='building',
            name='thematic',
            field=models.ForeignKey(default=1, to='StarGameApp.Thematic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='generaltechnology',
            name='thematic',
            field=models.ForeignKey(default=1, to='StarGameApp.Thematic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='race',
            name='thematic',
            field=models.ForeignKey(default=1, to='StarGameApp.Thematic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unit',
            name='thematic',
            field=models.ForeignKey(default=1, to='StarGameApp.Thematic'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='thematic',
            field=models.ForeignKey(default=1, to='StarGameApp.Thematic'),
            preserve_default=False,
        ),
    ]
