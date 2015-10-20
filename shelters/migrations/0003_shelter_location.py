# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0002_shelter_shelter_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, verbose_name='Location', blank=True),
        ),
    ]
