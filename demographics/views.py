from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse ,HttpResponseRedirect #generate http responses
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from matplotlib import pylab
from pylab import *
import PIL
import PIL.Image
import StringIO
import numpy as np


import json #for json encoding, decoding

from models import Age, Gender, Zipcode, User


numUsers = 1

def index(request):
    return HttpResponse("Hello World. You are at the poll index")

#receives incoming data from android about user demographics
@csrf_exempt
def receiveDataFromAndroid(request):
    print "Post from Android"
    global numUsers
    try:
        print "Request Body: ", request.body
        data = json.loads(request.body)
        print "Data: ", data
        z = str(data["Zip"])
        a = str(data["Age"])
        g = str(data["Gender"])
        #displays the age gender and zip code of the user on the console
        print "User is a ", g, " from ", z, "\nAge: ", a
        #uses premade zipcode, age and gender objects to help create a new user;
        #this does not work if the zipcodes, agegroups, and gender are not entered in the database to begin with
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

    #increments the count of the selected age group, the zip and the gender intered by the user
    selectedAgeGroup.ageCount += 1
    selectedZip.count += 1
    selectedGender.count += 1
    
    #creates a new user to store in the database
    u = User(zip=selectedZip, age=selectedAgeGroup, gender=selectedGender, userCount = numUsers)
    numUsers += 1
    u.save()
    selectedAgeGroup.save()
    selectedZip.save()
    selectedGender.save()
    #else:



    return HttpResponse("")
#displays a graph on a url mapped demographics/graph/
#does not work yet
# attach some text labels
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.05*height, '%d'%int(height),
                ha='center', va='bottom')
def graph(request):

    zipcodeList = Zipcode.objects.all()
    zipList = []
    zipCount = []
    for i in zipcodeList:

        zipList.append(int(i.zipcode))
        zipCount.append(int(i.count))
	print i.zipcode
	print i.count
    n_groups = len(zipList)
    index = np.arange(n_groups)
    rects1 = bar(index, zipCount, .25, alpha=.4, color = 'r', label="Zip Codes")

    #y = [5,2,6,7,8,9]

    #bar(zipList,zipCount)

    #bar(zipList,zipCount)

    xlabel('Zip Codes')
    ylabel('Users')
    title("Zip Codes Serviced by Sunstreet App")
    xticks(index+.25, zipList, rotation=69, fontsize=12)
    yticks(fontsize = 20)
    legend()
    tight_layout()

    #grid(True)

    autolabel(rects1)
    buffer = StringIO.StringIO()

    canvas = pylab.get_current_fig_manager().canvas
    canvas.draw()
    graphIMG = PIL.Image.frombytes("RGB", canvas.get_width_height(), canvas.tostring_rgb())
    graphIMG.save(buffer, "PNG")
    pylab.close()

    return HttpResponse(buffer.getvalue(), mimetype="image/png")


# Create your views here.
