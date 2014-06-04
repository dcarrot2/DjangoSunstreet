from django.db import models

# Create your models here.


class Zipcode(models.Model):
    zipcode = models.CharField(max_length=10)
    count = models.IntegerField(default=0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.zipcode

class Age(models.Model):
    age = models.CharField(max_length = 10)
    ageCount = models.IntegerField(default=0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.age

class Gender(models.Model):
    gender = models.CharField(max_length = 10)
    count = models.IntegerField(default = 0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.gender

class User(models.Model):
    zip = models.ForeignKey(Zipcode)
    age = models.ForeignKey(Age)
    gender = models.ForeignKey(Gender)
    userCount = models.IntegerField(default = 1)
    def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.userCount)


