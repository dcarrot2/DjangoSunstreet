from django.shortcuts import render
from events.models import Event
from django.http import HttpResponse
import json
import decimal
from django.db.models.base import ModelState
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def events_to_android(request):
    events = Event.objects.get_queryset()
    response = {}
    eventCount = 0
    if(events):
        for event in events:
            response[eventCount] = []
            response[eventCount].append({'event_title':event.title})
            response[eventCount].append({'event_youtube':event.youTube_link})
            response[eventCount].append({'event_description': event.description})
            response[eventCount].append({'event_date':json.dumps(event.date, cls=DateTimeEncoder)})
            response[eventCount].append({'event_url':event.link_to_event})

            #response['event_count']['event_youtube'] = event.youTube_link
            #esponse['event_count']['event_description'] = event.description
            #response['event_count']['event_date'] = event.date
            #response['event_count']['event_url'] = event.link_to_event
            eventCount+=1
        return HttpResponse(json.dumps(response), content_type="application/json")
    else:
        return HttpResponse("No data")

class DateTimeEncoder(json.JSONEncoder):
    def default(self, obj):
       if hasattr(obj, 'isoformat'):
           return obj.isoformat()
       elif isinstance(obj, decimal.Decimal):
           return float(obj)
       elif isinstance(obj, ModelState):
           return None
       else:
           return json.JSONEncoder.default(self, obj)