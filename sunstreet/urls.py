from django.conf.urls import patterns, include, url
import forms_builder.forms.urls

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sunstreet.views.home', name='home'),
    # url(r'^sunstreet/', include('sunstreet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^demographics/', include('demographics.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^botvin/', include('botvin_lifeskills.urls', namespace="botvin_lifeskills")),
    url(r'^topnews/', include('top_news.urls', namespace='top_news')),
    url(r'^forms/', include(forms_builder.forms.urls)),
    url(r'^events/', include('events.urls', namespace="events")),

)
