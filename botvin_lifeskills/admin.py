from django.contrib import admin
from botvin_lifeskills.models import Answer, Question, User, Botvin_User_Final
class UserAdmin(admin.ModelAdmin):

    list_display = ['school_code', 'date_survey_taken', 'section_a_questions', "section_b_questions",
                    'section_c_questions', 'section_d_questions']
    list_display = ['school_code']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question', 'section', 'school_level']

class RunAdmin(admin.ModelAdmin):
    list_display = ['user_key','school','date_taken']

admin.site.register(User, UserAdmin)
admin.site.register(Botvin_User_Final, RunAdmin)
