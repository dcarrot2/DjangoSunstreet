from django.conf.urls import patterns, url, include

from demographics import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'receivedatafromandroid/$', views.receiveDataFromAndroid, name='receivedatafromandroid' ),
    url(r'graph/$', views.graph, name='graph'),
)
