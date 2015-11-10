# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('StarGameApp', '0007_buildingsusers_generaltechnologiesusers_resource_resourcesusers_unitsusers'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelationBuildingsUsers',
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
            name='RelationGeneralTechnologiesUsers',
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
            name='RelationResourcesUsers',
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
            name='RelationUnitsUsers',
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
        migrations.RemoveField(
            model_name='buildingsusers',
            name='building',
        ),
        migrations.RemoveField(
            model_name='buildingsusers',
            name='user',
        ),
        migrations.DeleteModel(
            name='BuildingsUsers',
        ),
        migrations.RemoveField(
            model_name='generaltechnologiesusers',
            name='technology',
        ),
        migrations.RemoveField(
            model_name='generaltechnologiesusers',
            name='user',
        ),
        migrations.DeleteModel(
            name='GeneralTechnologiesUsers',
        ),
        migrations.RemoveField(
            model_name='resourcesusers',
            name='resource',
        ),
        migrations.RemoveField(
            model_name='resourcesusers',
            name='user',
        ),
        migrations.DeleteModel(
            name='ResourcesUsers',
        ),
        migrations.RemoveField(
            model_name='unitsusers',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='unitsusers',
            name='user',
        ),
        migrations.DeleteModel(
            name='UnitsUsers',
        ),
    ]
