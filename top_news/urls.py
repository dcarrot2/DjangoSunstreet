#django urls
from django.conf.urls import patterns, url

from top_news import views


urlpatterns = patterns('',

	url(r'^requestFromAndroid/$', views.requestFromAndroid, name='requestFromAndroid'),

)