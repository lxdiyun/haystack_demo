from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config

dajaxice_autodiscover()

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'haystack_demo.views.home', name='home'),
                       # url(r'^haystack_demo/', include('haystack_demo.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       #
                       url(dajaxice_config.dajaxice_url,
                           include('dajaxice.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^search/', include('haystack.urls')),
                       url(r'', include('myapp.urls')),
                       )
