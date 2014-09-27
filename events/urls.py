#django urls
from django.conf.urls import patterns, url

from events import views


urlpatterns = patterns('',

	url(r'^eventsToAndroid/$', views.events_to_android, name='events_to_android'),

)
