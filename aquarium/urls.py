from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from carriage import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'aquarium.views.home', name='home'),
    # url(r'^aquarium/', include('aquarium.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.IndexView.as_view(), name='index'),
    (r'^carriage/(?P<crg_id>[^/]+)/$','carriage.views.view_page'),
)
