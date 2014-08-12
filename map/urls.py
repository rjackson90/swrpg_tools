from django.conf.urls import patterns, include, url

urlpatterns = patterns('map.views', 
    url(r'^show/(\w+)/$', 'show'),
)
