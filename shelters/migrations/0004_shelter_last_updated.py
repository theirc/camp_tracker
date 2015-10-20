# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelters', '0003_shelter_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='shelter',
            name='last_updated',
            field=models.DateTimeField(null=True, verbose_name='Last Updated On', blank=True),
        ),
    ]
