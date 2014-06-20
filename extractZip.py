import os
import urllib2
from BeautifulSoup import BeautifulSoup
def populate():
    url = "http://www.mapszipcode.com/california/county/monterey"
    f = urllib2.urlopen(url).read()

    zipList = []

    soup = BeautifulSoup(f)

    for x in soup.findAll('a'):
        try:
            if(str(''.join(x.findAll(text=True)))[0] == "9"):
                zipList.append(str(''.join(x.findAll(text=True))[0:5]))
        except:
            print "Exception"
    for i in zipList:
        zipCodeModel = Zipcode.objects.get_or_create(zipcode=i)
    addGender("Male")
    addGender("Female")
    addAgeRange("9-13")
    addAgeRange("14-18")
    addAgeRange("19+")

    for a in Age.objects.all():
        print str(a)
    for a in Gender.objects.all():
        print str(a)
    for a in Zipcode.objects.all():
        print str(a), " ",

def addGender(gen):
    genderModel = Gender.objects.get_or_create(gender = gen)
    return genderModel
def addAgeRange(range):
    ageRangeObject = Age.objects.get_or_create(age=range)
    AgeRangeObj = Age_Range.objects.get_or_create(range= range)
    return ageRangeObject


if __name__ == '__main__':
    print "Adding information for Zipcodes, Gender, and Ages"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',"sunstreet.settings")
    from demographics.views import Age, Zipcode, Gender
    from top_news.models import Age_Range
    populate()

#print
#print "[",
#for x in zipList:
#    print x +", ",
#print"]"
#print len(zipList)

#print soup.prettify()

