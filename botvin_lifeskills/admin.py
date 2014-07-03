from django.contrib import admin
from botvin_lifeskills.models import User
class UserAdmin(admin.ModelAdmin):

    list_display = ['school_code', 'date_survey_taken']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question', 'section', 'school_level']

admin.site.register(User, UserAdmin)
