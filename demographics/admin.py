from django.contrib import admin
from demographics.models import Zipcode, User, Age, Gender
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['userCount', 'zip', 'age', 'gender']

#admin.site.register(Zipcode)
admin.site.register(User, UserAdmin)
