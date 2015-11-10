# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StarGameApp', '0006_auto_20150318_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingsUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amoung', models.IntegerField()),
                ('building', models.ForeignKey(to='StarGameApp.Building')),
                ('user', models.ForeignKey(to='StarGameApp.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='GeneralTechnologiesUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField()),
                ('technology', models.ForeignKey(to='StarGameApp.GeneralTechnology')),
                ('user', models.ForeignKey(to='StarGameApp.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('thematic', models.ForeignKey(to='StarGameApp.Thematic')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResourcesUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amoung', models.FloatField()),
                ('resource', models.ForeignKey(to='StarGameApp.Resource')),
                ('user', models.ForeignKey(to='StarGameApp.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UnitsUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('amoung', models.IntegerField()),
                ('unit', models.ForeignKey(to='StarGameApp.Unit')),
                ('user', models.ForeignKey(to='StarGameApp.UserProfile')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
