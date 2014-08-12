from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from swrpg import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'swrpg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^map/', include('map.urls')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root':settings.MEDIA_ROOT}),

)
