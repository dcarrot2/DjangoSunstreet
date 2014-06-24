from django.contrib import admin
from lifeskills.models import PreTestQuestion, PreTestAnswer, PreTestUser, PostTestQuestion, PostTestAnswer, PostTestUser



class LifeSkillsPreAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_question','second_question']

class PreTestQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question']

class PreTestAnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'choices','votes']

class LifeSkillsPostAdmin(admin.ModelAdmin):
    list_display = ['posttestuser_num', 'question_one', 'question_two', 'question_three', 'question_four',
                    'question_five','question_six','question_seven','question_eight']

class PostTestQuestionAdmin(admin.ModelAdmin):
    list_display = ['question_number', 'question', 'isTextField']

class PostTestAnswerAdmin(admin.ModelAdmin):
    list_display = ['question', 'choices', 'votes']


admin.site.register(PreTestUser, LifeSkillsPreAdmin)
admin.site.register(PostTestUser, LifeSkillsPostAdmin)

