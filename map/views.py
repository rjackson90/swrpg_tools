from django.shortcuts import render_to_response
from django.http import HttpResponse

from map.models import Map

def show(request, map_id):
    try:
        m = Map.objects.get(str_id=map_id)
    except Map.DoesNotExist:
        raise Http404
    return render_to_response("map/show.html", {'map' : m})
