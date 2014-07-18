from django.db import models

# Create your models here.

#model stores the zipcode and stores the count of the zipcode
class Zipcode(models.Model):
    zipcode = models.CharField(max_length=10)
    count = models.IntegerField(default=0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.zipcode
#model stores the age range and stores the count of the age range
class Age(models.Model):
    age = models.CharField(max_length = 10)
    ageCount = models.IntegerField(default=0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.age
#model stores the two possible genders and keeps count of the user that select that gender
class Gender(models.Model):
    gender = models.CharField(max_length = 10)
    count = models.IntegerField(default = 0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.gender
#model stores the specific user, gives it a value beginning at 1 then stores the users zip, age, and gender
class User(models.Model):
    zip = models.ForeignKey(Zipcode)
    age = models.ForeignKey(Age)
    gender = models.ForeignKey(Gender)
    userCount = models.IntegerField(default = 1)
    date = models.DateTimeField("date added")
    def __unicode__(self):  # Python 3: def __str__(self):
        return str(self.date)


