from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from top_news.models import Age_Range, News_Article
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.core import serializers
import json
import datetime
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def requestFromAndroid(request):
    print "Post from android"
    try:
        data = json.loads(request.body)
        print "Data: ", data
        range = data["age_range"]
    except:
        print "Exception. Could Not Parse JSON\n"

    newsArticles = serializers.serialize("json", News_Article.objects.get_queryset().filter(range))

    print "Dump: ", newsArticles
    return HttpResponse(newsArticles)