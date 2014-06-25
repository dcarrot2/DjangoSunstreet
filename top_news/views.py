from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.core import serializers
from top_news.models import News_Article, Age_Range

import json


@csrf_exempt
def requestFromAndroid(request):
    print "Post from android"
    try:
        data = json.loads(request.body)
        print "Data: ", data
        range = data["Age"]
        print "Range: ", range
            # range = "19+"
        r = Age_Range.objects.get_queryset().filter(range=range)
        r = News_Article.objects.get_queryset().filter(age_range=r)
        response = {}
        for i in r:
            print i
            response[str(i.title)] = str(i.link)

    # newsArticles = serializers.serialize("json", News_Article.objects.get_queryset().filter(age_range=r))

        print "Dump: ", response
        return HttpResponse(json.dumps(response), content_type="application/json")

    except:
        print "Exception. Could Not Parse JSON\n"
        return  HttpResponse("")

