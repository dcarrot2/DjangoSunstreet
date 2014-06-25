from django.db import models


# Create your models here.
class Age_Range(models.Model):
    range = models.CharField(max_length = 10)

    def __unicode__(self):
        return self.range
    
    class Meta:
        verbose_name = "Age Range"

class News_Article(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField()
    age_range = models.ForeignKey(Age_Range)

    def __unicode__(self):
        return self.title
    
    class Meta:
        verbose_name = "News Article"
