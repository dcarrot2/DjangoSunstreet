from django.db import models

# Create your models here.


class Zipcode(models.Model):
    zipcode = models.CharField(max_length=10)
    count = models.IntegerField(default=0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.zipcode

class Person(models.Model):
    #age = models.CharField(max_length = 10)
    #ageCount = models.IntegerField(default=0)
    #MaleOrFemale = models.CharField(max_length = 10)
    #maleCount = models.IntegerField(default = 0)
    #femaleCount = models.IntegerField(default = 0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.age

