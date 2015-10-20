# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('camp_id', models.PositiveIntegerField(default=-1, null=True, verbose_name='Camp Identifier')),
                ('camp_name', models.CharField(max_length=200, verbose_name='Camp Name', blank=True)),
                ('camp_polygon', django.contrib.gis.db.models.fields.PolygonField(srid=4326, null=True, verbose_name='Camp Polygon', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.PositiveIntegerField(null=True, verbose_name='Type of Shelter', choices=[(1, 'Tent'), (2, 'House'), (3, 'Other')])),
                ('capacity', models.PositiveIntegerField(default=0, null=True, verbose_name='Capacity')),
                ('occupants', models.PositiveIntegerField(default=0, null=True, verbose_name='Current Number of Occupants')),
                ('camp', models.ForeignKey(verbose_name='Camp', to='shelters.Camp')),
            ],
        ),
    ]
