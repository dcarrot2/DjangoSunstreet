from django.db import models

from django.utils import timezone

# Create your models here.
class School(models.Model):
    school_code = models.CharField(max_length=15)
    count = models.IntegerField(default=0)
    def __unicode__(self):
        return self.school_code



class Botvin_Section(models.Model):
    section_letter = models.CharField(max_length = 2)
    school_level = models.CharField(max_length = 3)
    #user = models.ForeignKey(User)
    def __unicode__(self):
        return self.section_letter

class User(models.Model):

        school_code = models.ForeignKey(School)
        date_survey_taken = models.DateTimeField('date published')
        myList = models.TextField(null = True)
        num_questions_answered = models.IntegerField()

        school_level = models.CharField(max_length=3)

        # section_a_questions = models.ForeignKey(Botvin_Section, related_name = "sectionaquestions")
        # section_b_questions = models.ForeignKey(Botvin_Section, related_name = "sectionbquestions")
        # section_c_questions = models.ForeignKey(Botvin_Section, related_name = "sectioncquestions")
        # section_d_questions = models.ForeignKey(Botvin_Section, related_name = "sectiondquestions")


        #list that will eventually hold Botvin Answer type objects made by the user.


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
    date_taken = models.DateTimeField('date published')

#===============================================================================
# class Choice(models.Model):
#     user = models.ForeignKey(User)
#     selection = models.ForeignKey(Answer)
#===============================================================================

