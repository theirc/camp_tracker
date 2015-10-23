from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from django.shortcuts import render_to_response
from django.template import RequestContext

from . import models
import json


def index(request):
    shelters = models.Shelter.objects.order_by('occupants')
    serialized = [{
        "camp_id": s.camp.id,
        "type": s.get_type_display(),
        "shelter_id": s.shelter_id,
        "location": {"coordinates": [s.location.x, s.location.y]}, #json.loads(s.location.json),
        "occupants": s.occupants,
    } for s in shelters]

    c = models.Camp.objects.get(camp_id=1)

    camp = {
        "name": c.camp_name,
    }

    return render_to_response("index.html", {
        "shelters": json.dumps(serialized),
        "camp": json.dumps(camp),
    }, RequestContext(request))

def list(request):
    shelters = models.Shelter.objects.order_by('occupants', 'type', 'shelter_id ')
    return render_to_response("list.html", {
        "shelters": shelters,
    }, RequestContext(request))
