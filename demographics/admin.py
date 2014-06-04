from django.contrib import admin
from demographics.models import Zipcode, User, Age, Gender
from lifeskills.models import PreTestQuestion, PreTestAnswer, PreTestUser, PostTestQuestion, PostTestAnswer, PostTestUser
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ['userCount', 'zip', 'age', 'gender']

class LifeSkillsPreAdmin(admin.ModelAdmin):
    list_display = ['preuser_num', 'question_one', 'question_two', 'question_three', 'question_four',
                    'question_five','question_six','question_seven','question_eight']

class LifeSkillsPostAdmin(admin.ModelAdmin):
    list_display = ['postuser_num', 'first_question','second_question']

class PreTestQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question']

class PreTestAnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'choice_text']

admin.site.register(User, UserAdmin)
admin.site.register(PostTestQuestion)
admin.site.register(PostTestAnswer)
admin.site.register(PreTestUser, LifeSkillsPreAdmin)
admin.site.register(PostTestUser, LifeSkillsPostAdmin)
admin.site.register(PreTestQuestion, PreTestQuestionAdmin)
admin.site.register(PreTestAnswer, PreTestAnswerAdmin)
