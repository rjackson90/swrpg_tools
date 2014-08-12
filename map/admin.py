from django.contrib import admin
from map.models import Map

# Register your models here.

class MapAdmin(admin.ModelAdmin):
    pass
admin.site.register(Map, MapAdmin)
