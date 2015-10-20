from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from rest_framework import authentication, permissions, viewsets

from .. import models
from . import serializers

class DefaultsMixin(object):
    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class CampViewSet(viewsets.ModelViewSet, DefaultsMixin):
    queryset = models.Camp.objects.all()
    serializer_class = serializers.CampSerializer

class ShelterViewSet(viewsets.ModelViewSet, DefaultsMixin):
    queryset = models.Shelter.objects.all()
    serializer_class = serializers.ShelterSerializer