from django.db import models


# Create your models here.
class Age_Range(models.Model):
    range = models.CharField(max_length = 10)

    def __unicode__(self):
        return self.range

class News_Article(models.Model):
    title = models.CharField(max_length=20)
    link = models.URLField()
    age_range = models.ForeignKey(Age_Range)

    def __unicode__(self):
        return self.title
