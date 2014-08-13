from django.conf.urls import patterns, include, url

urlpatterns = patterns('map.views', 
    url(r'^map/(\w+)/$', 'map'),
    url(r'^character/(\w+)/$', 'character'),
    url(r'^encounter/(\w+)/$', 'encounter'),
)
