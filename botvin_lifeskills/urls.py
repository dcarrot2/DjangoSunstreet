from django.conf.urls import patterns, url

from botvin_lifeskills import views

urlpatterns = patterns('',

	url(r'^section/(?P<section>\D+)/(?P<school_level>\D+)$', views.botvinSection, name='botvinsurvey'),

    url(r'^section/botvinVote/$', views.botvinSectionVote, name="botvinSectionVote"),

    url(r'^section/results/$', views.results, name="results"),

)
