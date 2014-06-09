from django.contrib import admin
from botvin_lifeskills.models import Answer, Question, User, Botvin_Section

class UserAdmin(admin.ModelAdmin):
    list_display = ['student_code', 'school_code', 'date_survey_taken', 'section_a_questions', "section_b_questions",
                    'section_c_questions', 'section_d_questions']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question', 'section', 'school_level']
admin.site.register(User, UserAdmin)
#admin.site.register(Question, QuestionAdmin)

# Register your models here.
