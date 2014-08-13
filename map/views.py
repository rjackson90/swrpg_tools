from django.shortcuts import render_to_response
from django.http import HttpResponse

from map.models import Map, Character, Encounter

def map(request, map_slug):
    try:
        m = Map.objects.get(str_id=map_slug)
    except Map.DoesNotExist:
        raise Http404
    return render_to_response("map/map.html", {'map' : m})

def character(request, char_slug):
    try:
        char = Character.objects.get(slug=char_slug)
    except Character.DoesNotExist:
        raise Http404
    return render_to_response("map/character.html", {"character" : char})


def encounter(request, encounter_slug):
    try:
        encounter = Encounter.objects.get(slug=encounter_slug)
    except Encounter.DoesNotExist:
        raise Http404
    return render_to_response("map/encounter.html",
            {
                "encounter" : encounter,
                "map" : encounter.scene,
                "characters" : encounter.characters.all()
            })

