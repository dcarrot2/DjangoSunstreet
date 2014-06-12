from django.db import models

from django.utils import timezone

# Create your models here.


class Botvin_Section(models.Model):
    section_letter = models.CharField(max_length = 2)
    school_level = models.CharField(max_length = 3)
    #user = models.ForeignKey(User)
    def __unicode__(self):
        return self.section_letter

class User(models.Model):
        student_code = models.IntegerField()
        school_code = models.IntegerField()
        #date_survey_taken = models.DateTimeField('date published')
        myList = models.TextField(null = True)
        num_questions_answered = models.IntegerField()
        
        school_level = models.CharField(max_length=3)

        # section_a_questions = models.ForeignKey(Botvin_Section, related_name = "sectionaquestions")
        # section_b_questions = models.ForeignKey(Botvin_Section, related_name = "sectionbquestions")
        # section_c_questions = models.ForeignKey(Botvin_Section, related_name = "sectioncquestions")
        # section_d_questions = models.ForeignKey(Botvin_Section, related_name = "sectiondquestions")

        
        #list that will eventually hold Botvin Answer type objects made by the user.
       

        def __unicode__(self):
            return "Student: " + str(self.student_code) + " School:" + str(self.school_code)

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

class Botvin_User_Section(models.Model):
    section_letter = models.CharField(max_length = 3)
    school_level = models.CharField(max_length = 3)
    student_code = models.IntegerField()
    answer_list = models.TextField(null=True)


#===============================================================================
# class Choice(models.Model):
#     user = models.ForeignKey(User)
#     selection = models.ForeignKey(Answer)
#===============================================================================
    
