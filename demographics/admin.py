from django.contrib import admin
from demographics.models import Zipcode, User, Age, Gender
from lifeskills.models import Question, Answer
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['userCount', 'zip', 'age', 'gender']

admin.site.register(User, UserAdmin)
admin.site.register(Question)
admin.site.register(Answer)
