from django.db import models

from django.utils import timezone

class School(models.Model):
    school_code = models.CharField(max_length=15)
    count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.school_code



class Botvin_Section(models.Model):
    section_letter = models.CharField(max_length = 2)
    school_level = models.CharField(max_length = 3)
    
    def __unicode__(self):
        return self.section_letter

class User(models.Model):

        school_code = models.ForeignKey(School)
        date_survey_taken = models.DateTimeField('date published')
        myList = models.TextField(null = True)
        num_questions_answered = models.IntegerField()

        school_level = models.CharField(max_length=3)
        def __unicode__(self):
            return "School:" + str(self.school_code) + " Date survey taken: " + str(self.date_survey_taken)

class Question(models.Model):
    section = models.ForeignKey(Botvin_Section)
    question = models.CharField(max_length=200)
    question_number = models.IntegerField()
    section_letter = models.CharField(max_length=4)
    school_level = models.CharField(max_length=4)


    def __unicode__(self):
        return self.question


class Answer(models.Model):
    answer = models.ForeignKey(Question)
    choices = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __unicode__(self):
        return self.choices


class Botvin_User_Run(models.Model):
    user_key = models.CharField(max_length=50)
    school = models.CharField(max_length=50)
    school_level = models.CharField(max_length=2)
    answer_set = models.ManyToManyField(Answer)
    def __unicode__(self):
        return self.user_key

class Botvin_User_Final(models.Model):
    user_key = models.CharField(max_length=50)
    school_level = models.CharField(max_length=3)
    school = models.CharField(max_length=50)
    answer_set = models.ManyToManyField(Answer)
    date_taken = models.DateTimeField('date taken')

    class Meta:
        verbose_name = "Botvin User"



