from django.db import models

# Create your models here.
class PreTestQuestion(models.Model):
	question = models.CharField(max_length=200)
	question_number = models.IntegerField(default=1)
	
	def __unicode__(self):
		return self.question
class PreTestAnswer(models.Model):
	answer = models.ForeignKey(PreTestQuestion)
	choices = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.choices



class PreTestUser(models.Model):
        preuser_num = models.IntegerField(default=1)
        question_one = models.ForeignKey(PreTestAnswer, related_name = 'pretestuser_questionone')
        question_two = models.ForeignKey(PreTestAnswer, related_name = 'pretestuser_questiontwo')
        question_three = models.ForeignKey(PreTestAnswer, related_name = 'pretestuser_questionthree')
        question_four = models.ForeignKey(PreTestAnswer, related_name = 'pretestuser_questionfour')
        question_five = models.ForeignKey(PreTestAnswer, related_name = 'pretestuser_questionfive')
        question_six = models.ForeignKey(PreTestAnswer, related_name = 'pretestuser_questionsix')
        question_seven = models.ForeignKey(PreTestAnswer, related_name = 'pretestuser_questionseven')
        question_eight = models.ForeignKey(PreTestAnswer, related_name = 'pretestuser_questioneight')

class PostTestQuestion(models.Model):
        question = models.CharField(max_length=200)
        question_number = models.IntegerField(default=1)

        def __unicode__(self):
                return self.question


class PostTestAnswer(models.Model):
        question = models.ForeignKey(PostTestQuestion)
        choices = models.CharField(max_length=200)
        votes  = models.IntegerField(default=0)

        def __unicode__(self):
                return self.choice_text

class PostTestUser(models.Model):
        postuser_num = models.IntegerField(default=1)
        first_question = models.ForeignKey(PostTestAnswer, related_name = 'posttestuser_firstquestion')
        second_question = models.ForeignKey(PostTestAnswer, related_name = 'posttestuser_secondquestion')
