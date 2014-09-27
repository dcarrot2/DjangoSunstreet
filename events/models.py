from django.db import models

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    youTube_link = models.URLField(blank=True)
    description = models.TextField()
    link_to_event = models.URLField(blank=True)

    def __unicode__(self):
        return self.title

