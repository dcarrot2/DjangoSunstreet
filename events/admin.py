from django.contrib import admin
from events.models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'youTube_link','description', 'link_to_event']

admin.site.register(Event, EventAdmin)