from django.contrib import admin
from map.models import Map, Character, Encounter

# Register your models here.

class MapAdmin(admin.ModelAdmin):
    pass
admin.site.register(Map, MapAdmin)

class CharacterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Character, CharacterAdmin)

class EncounterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Encounter, EncounterAdmin)
