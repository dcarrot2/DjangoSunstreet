from django.contrib import admin
from demographics.models import Zipcode, Person
from lifeskills.models import Question, Answer
# Register your models here.

admin.site.register(Zipcode)
admin.site.register(Person)
admin.site.register(Question)
admin.site.register(Answer)
