from django.contrib import admin
from botvin_lifeskills.models import Answer, Question, User

class UserAdmin(admin.ModelAdmin):
    list_display = ['student_code', 'school_code', 'date_survey_taken']

admin.site.register(User, UserAdmin)
#### Register your models here.
