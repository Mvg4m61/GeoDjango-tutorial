from django.shortcuts import render

from django.views import generic
from django.contrib.gis.geos import fromstr, Point
from django.contrib.gis.db.models.functions import Distance
from .models import Shop

longitude = 36.825474
latitude = -1.285035

user_location = Point(longitude, latitude, srid=4326)

class Home(generic.ListView):
    model = Shop
    context_object_name = 'shops'
    queryset = Shop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'index.html'