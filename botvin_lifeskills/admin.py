from django.contrib import admin
from botvin_lifeskills.models import Answer, Question, User

class UserAdmin(admin.ModelAdmin):
    list_display = ['student_code', 'school_code', 'date_survey_taken', 'section_a_question', "section_b_question",
                    'section_c_question', 'section_d_question']

admin.site.register(User, UserAdmin)

# Register your models here.
