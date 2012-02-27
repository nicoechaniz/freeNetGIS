from django.conf.urls.defaults import patterns, include, url
from django.contrib.gis import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^mysite/', include('mysite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^nodes/', include('apps.nodes.urls')),
    url(r'^maps/', include('apps.maps.urls')),
    url(r'^api/', include('apps.api.urls')),
)


urlpatterns += patterns('django.views',
        (r'site_media/(.*)$', 'static.serve', {'document_root':
settings.MEDIA_ROOT}), )

