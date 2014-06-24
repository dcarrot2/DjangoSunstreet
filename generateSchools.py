import os
import urllib2
from BeautifulSoup import BeautifulSoup


def populateHsList():
    url = "http://www.monterey.k12.ca.us/home/districts-and-schools/links#Districts"
    f = urllib2.urlopen(url).read()
    schoolList = []
    soup = BeautifulSoup(f)
    count = 0
    for x in soup.findAll('tr'):
        try:
            if( count > 26 and count <= 158):
                # print count
                # print x.findAll('td',text=True)[1],"\n\n"
                schoolList.append(str(x.findAll('td',text=True)[1]))
            count+=1

        except:
            print "Exception"
    schoolList[27] = "Community Day School"

    for element in schoolList:
        s = School.objects.get_or_create(school_code = element)
    return
if __name__ == '__main__':
    print "Adding Highschool Information"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',"sunstreet.settings")
    from botvin_lifeskills.models import School
    populateHsList()