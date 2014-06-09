from django.conf.urls import patterns, url

from lifeskills import views


urlpatterns = patterns('',

	url(r'^pretest/$', views.pretest, name='pretest'),
        url(r'^pretestvote/$', views.pretestvote, name="pretestvote"),
	url(r'^posttest/$', views.posttest, name='posttest'),
	url(r'^posttestvote/$', views.posttestvote, name= "posttestvote"),
	url(r'^response/$', views.response, name = "response"),

)
