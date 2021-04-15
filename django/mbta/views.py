"""mbta views"""
from django.shortcuts import render

from mbta.models import MBTARoute, MBTAStop

# Create your views here.

def index(request):
    """index page for mbta app"""
    context = {}

    routes = MBTARoute().get(filters={'type':[MBTARoute.Type.LIGHT_RAIL, MBTARoute.Type.HEAVY_RAIL]})
    routes = routes.json()['data']
    context["routes"] = routes

    stops = MBTAStop().get(filters={'route':[r['id'] for r in routes]})
    stops = stops.json()['data']
    context["stops"] = stops

    return render(request, 'mbta/index.html', context)
