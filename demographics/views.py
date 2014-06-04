from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect #generate http responses
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
import json #for json encoding, decoding

from models import Age, Gender, Zipcode, User

numUsers = 1

def index(request):
    return HttpResponse("Hello World. You are at the poll index")

@csrf_exempt
def recieveDataFromAndroid(request):
    print "Post from Android"
    global numUsers
    try:
        print "Request Body: ", request.body
        data = json.loads(request.body)
        print "Data: ", data
        z = str(data["Zip"])
        a = str(data["Age"])
        g = str(data["Gender"])
        print "User is a ", g, " from ", z, "\nAge: ", a
        selectedZip = Zipcode.objects.get(zipcode = z)
       # print selectedZip
        selectedAgeGroup = Age.objects.get(age= a)
       # print selectedAgeGroup
        selectedGender = Gender.objects.get(gender= g)
       # print selectedGender
        #z = Zipcode(zipcode = z)
        #a = Age(age = a)
        #g = Gender(gender = g)

    except:
        print "Exception. Could Not Parse JSON\n"


    selectedAgeGroup.ageCount += 1
    selectedZip.count += 1
    selectedGender.count += 1

    u = User(zip=selectedZip, age=selectedAgeGroup, gender=selectedGender, userCount = numUsers)
    numUsers += 1
    u.save()
    #else:



    return HttpResponse("")


# Create your views here.
