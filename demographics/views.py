from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect #generate http responses
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import json #for json encoding, decoding

from models import Age, Gender, Zipcode, User

def index(request):
    return HttpResponse("Hello World. You are at the poll index")

def recieveDataFromAndroid(request):
    print "Post from Android"

    try:
        print "Request Body: ", request.body
        data = json.loads(request.body)
        print "Data: ", data
        z = data["zip"]
        a = data["age"]
        g = data["gender"]
        print "User is a ", g, " from ", z, "\nAge: ", a
        selectedZip = Zipcode.objects.get(zipcode = z)
        selectedAgeGroup = Age.objects.get(age= a)
        selectedGender = Gender.objects.get(gender= g)

    except:
        print "Exception. Could Not Parse JSON\n"

    selectedGender.count += 1
    selectedAgeGroup.ageCount += 1
    selectedZip.count += 1

    u = User(zip=z, age=a, gender=g)
    u.userCount+=1
    u.save()
    return HttpResponse("")


# Create your views here.
