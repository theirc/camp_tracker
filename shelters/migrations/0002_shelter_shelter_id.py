# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='shelter_id',
            field=models.CharField(max_length=100, null=True, verbose_name='Shelter Identifier', blank=True),
        ),
    ]
