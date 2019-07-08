from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.http import Http404, JsonResponse
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.core.serializers import serialize
from django.views.generic import TemplateView
import json
import requests
from owslib.wfs import WebFeatureService

from .models import WorldBorder

#from .models import Choice, Question

class MapsView(TemplateView):
    template_name = 'world/maps3.html'

def index(request):
    return render(request, 'world/index.html')

def maps(request):
    #return HttpResponse("You're looking at a maps.")
    #map_as_geojson = serialize('geojson', WorldBorder.objects.all())
    #return JsonResponse(json.loads(map_as_geojson))
    wfsgeo = WebFeatureService(url='http://139.59.68.199/geoserver/wms', version='1.0.0')
    context = { 
        'elements': list(wfsgeo.contents),
    }
    return render(request, 'world/maps4.html', context)

def downloads(request):
    wfsgeo = WebFeatureService(url='http://139.59.68.199/geoserver/wms', version='1.0.0')
    context = { 
        'elements': list(wfsgeo.contents),
    }
    return render(request, 'world/downloads.html', context)

def fileDown(request, layer_name):
    wfsgeo = WebFeatureService(url='http://139.59.68.199/geoserver/wms', version='1.1.0')
    #res = wfsgeo.getfeature(typename=layer_name, bbox=(4500000,5500000,4500500,5500500), srsname='urn:x-ogc:def:crs:EPSG:31468')
    return HttpResponse("layer name is " + layer_name)