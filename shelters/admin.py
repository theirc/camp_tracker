from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from django.contrib.gis import admin
from . import models


class ShelterAdmin(admin.GeoModelAdmin):
    list_display = ('camp', 'shelter_id', 'occupants', 'capacity')


admin.site.register(models.Camp, admin.GeoModelAdmin)
admin.site.register(models.Shelter, ShelterAdmin)