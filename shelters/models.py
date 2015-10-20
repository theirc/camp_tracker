from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _

SHELTER_TYPE = (
    (1, _('Tent')),
    (2, _('House')),
    (3, _('Other')),
)


class Camp(models.Model):
    camp_id = models.PositiveIntegerField(null=True, default=-1, verbose_name=_("Camp Identifier"), )
    camp_name = models.CharField(max_length=200, blank=True, verbose_name=_("Camp Name"))

    camp_polygon = models.PolygonField(null=True, blank=True, verbose_name=_("Camp Polygon"))

    def __unicode__(self):
        return self.camp_name or ' '


class Shelter(models.Model):
    camp = models.ForeignKey(Camp, verbose_name=_("Camp"))
    shelter_id = models.CharField(null=True, verbose_name=_("Shelter Identifier"), max_length=100, blank=True)
    type = models.PositiveIntegerField(null=True, verbose_name=_("Type of Shelter"), choices=SHELTER_TYPE)
    capacity = models.PositiveIntegerField(null=True, default=0, verbose_name=_("Capacity"))
    occupants = models.PositiveIntegerField(null=True, default=0, verbose_name=_("Current Number of Occupants"))
    location = models.PointField(null=True, blank=True, verbose_name=_("Location"))
    last_updated = models.DateTimeField(null=True, blank=True, verbose_name=_("Last Updated On"))