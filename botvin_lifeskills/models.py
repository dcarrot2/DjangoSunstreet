from django.db import models

from django.utils import timezone

# Create your models here.

class User(models.Model):
        student_code = models.IntegerField()
        school_code = models.IntegerField()
        date_survey_taken = models.DateTimeField('date published')
 #       section_a_questions = models.ForeignKey(Question)
  #      section_b_questions = models.ForeignKey(Question)
   #     section_c_questions = models.ForeignKey(Question)
    #    section_d_questions = models.ForeignKey(Question)

class Botvin_Section(models.Model):
    section_letter = models.CharField(max_length = 2)
    school_level = models.CharField(max_length = 3)
    use = models.ForeignKey(User)

class Question(models.Model):
    section = models.ForeignKey(Botvin_Section)
    question = models.CharField(max_length=200)
    question_number = models.IntegerField()
    section = models.CharField(max_length=4)
    school_level = models.CharField(max_length=4)


    def __unicode__(self):
        return self.question


class Answer(models.Model):
    answer = models.ForeignKey(Question)
    choices = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choices
