from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from rest_framework import serializers

from .. import models
import json


class CampSerializer(serializers.ModelSerializer):
    camp_polygon = serializers.SerializerMethodField()

    def get_camp_polygon(self, obj):
        return json.loads(obj.camp_polygon.json)

    class Meta:
        model = models.Camp
        fields = ('id', 'camp_id', 'camp_name', 'camp_polygon', )


class ShelterSerializer(serializers.ModelSerializer):
    location = serializers.SerializerMethodField()

    def get_location(self, obj):
        return json.loads(obj.location.json)

    class Meta:
        model = models.Shelter
        fields = ('id', 'camp', 'shelter_id', 'type', 'occupants', 'location' )