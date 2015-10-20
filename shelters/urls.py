from __future__ import absolute_import, unicode_literals, division, print_function

__author__ = 'reyrodrigues'

from rest_framework.routers import DefaultRouter

from .api import viewsets


router = DefaultRouter()
router.register(r'camps', viewsets.CampViewSet)
router.register(r'shelters', viewsets.ShelterViewSet)

from django.conf.urls import include, url
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    url(r'^api/token/', obtain_auth_token, name='api-token'),
    url(r'^api/', include(router.urls)),
    url(r'^list/?', views.list),
    url(r'/?', views.index),
]