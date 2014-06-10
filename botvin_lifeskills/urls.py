from django.conf.urls import patterns, url

from botvin_lifeskills import views

urlpatterns = patterns('',

	url(r'^section/(?P<section>\D+)/(?P<school_level>\D+)$', views.botvinSection, name='sectionAHSBotvin'),

        url(r'^section/(?P<section>\D+)/(?P<school_level>\D+)/botvinSectionVote/$', views.botvinSectionVote, name="botvinSectionVote"),

)
