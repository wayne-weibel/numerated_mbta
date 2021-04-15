"""mbta ajax"""
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseNotFound, JsonResponse

from mbta.models import MBTAPrediction, MBTAStop

def departure_prediction(request):
    """get prediction"""
    route_id = request.POST.get('route_id')
    if not route_id:
        return HttpResponseForbidden('Please select a Route')

    direction_id = request.POST.get('direction_id')
    if not direction_id:
        return HttpResponseForbidden('Please select a Direction')

    stop_id = request.POST.get('stop_id')
    if not stop_id:
        return HttpResponseForbidden('Please select a Stop')

    predictions = MBTAPrediction().get(route_id, direction_id, stop_id)
    departure = next((p['attributes']['departure_time'] for p in predictions.json()['data'] if p['attributes']['departure_time']), None)
    if not departure:
        return HttpResponseNotFound('Unable to predicte Departure')

    return HttpResponse(departure)

def stops_by_route(request):
    """get stops by route"""
    stops = MBTAStop().get(filters={'route':request.POST.get('route_id')})
    stops = stops.json()['data']

    return JsonResponse({'stops': stops})
