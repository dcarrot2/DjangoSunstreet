from django.contrib import admin
from demographics.models import Zipcode, User, Age, Gender
from lifeskills.models import PreTestQuestion, PreTestAnswer, PreTestUser, PostTestQuestion, PostTestAnswer, PostTestUser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['userCount', 'zip', 'age', 'gender']

admin.site.register(User, UserAdmin)




