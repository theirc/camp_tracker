from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

import requests

from django.core.management.base import BaseCommand
from django.conf import settings

from django.contrib.gis import geos
from shelters import models
from dateutil import parser


class Command(BaseCommand):
    help = 'Load Shelter Information from KoBo'

    def handle(self, *args, **options):
        kobo_url = getattr(settings, "KOBO_BASE_URL", "https://kc.humanitarianresponse.info/api/v1/data/")
        kobo_occupants_id = getattr(settings, "KOBO_OCCUPANTS_ID", 32175)
        kobo_shelter_form_id = getattr(settings, "KOBO_SHELTER_ID", 32042)
        kobo_username = getattr(settings, "KOBO_USERNAME", "")
        kobo_password = getattr(settings, "KOBO_PASSWORD", "")

        shelter_request = requests.get("{}{}".format(kobo_url, kobo_shelter_form_id),
                                       headers={"Accept": "application/json"},
                                       auth=(kobo_username, kobo_password))

        shelter_data = shelter_request.json()

        occupants_request = requests.get("{}{}".format(kobo_url, kobo_occupants_id),
                                         headers={"Accept": "application/json"},
                                         auth=(kobo_username, kobo_password))

        occupants_data = occupants_request.json()

        shelter_type_dict = {
            "tent": 1,
            "house": 2,
            "other": 3,
        }

        camp_dict = {}

        for d in [a for a in shelter_data if 'shelter/gps_location' in a and a["shelter/gps_location"]]:
            gps = [float(a) for a in d['shelter/gps_location'].split(' ')]
            camp_id = int(d['camp_id'])
            shelter_key = d['shelter/type_of_shelter'] + ' ' + d['shelter/Shelter_Identifier']
            shelter_id = d['shelter/Shelter_Identifier']
            shelter_type = shelter_type_dict[d['shelter/type_of_shelter']]

            point = geos.Point(gps[1], gps[0])
            if shelter_key not in camp_dict:
                camp_dict[shelter_key] = []

            camp_dict[shelter_key].append({
                "camp_id": camp_id,
                "shelter_id": shelter_id,
                "shelter_type": shelter_type,
                "point": point,
            })

        for k, v in camp_dict.iteritems():
            if len(v) == 1:
                # only one point
                point = v[0]["point"]
            elif len(v) == 2:
                # 2 points make a line and get the centroid
                line = geos.LineString([a['point'] for a in v])
                point = line.centroid
            elif len(v) > 2:
                # polygon!
                polygon = geos.Polygon([a['point'] for a in v])
                point = polygon.centroid
            if v:
                info = v[0]
                camp_id = info['camp_id']
                shelter_id = info['shelter_id']
                shelter_type = info['shelter_type']

                camp = models.Camp.objects.get(camp_id=camp_id)
                shelter, other = models.Shelter.objects.get_or_create(shelter_id=shelter_id, type=shelter_type, camp=camp)
                shelter.type = shelter_type
                shelter.camp = camp
                shelter.location = point
                shelter.save()

        for d in sorted(occupants_data, key=lambda k: k['end'], reverse=True):
            shelter_type = shelter_type_dict[d['shelter/type_of_shelter']]
            shelter = models.Shelter.objects.filter(shelter_id=d['shelter/Shelter_Identifier'], type=shelter_type)
            if shelter:
                shelter = shelter[0]
                end = parser.parse(d['end'])
                if not shelter.last_updated or shelter.last_updated < end:
                    if d['shelter/Is_this_shelter_empty'] == '0':
                        # Empty shelter
                        shelter.occupants = 0
                    else:
                        number_of_people = int(d['Number_of_People_in_Shelter'])
                        shelter.occupants = number_of_people
                    shelter.last_updated = end
                    shelter.save()

