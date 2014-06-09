from django.db import models

# Create your models here.
class PreTestQuestion(models.Model):
        question = models.CharField(max_length=200)
        question_number = models.IntegerField(default=1)

        def __unicode__(self):
                return self.question


class PreTestAnswer(models.Model):
        question = models.ForeignKey(PreTestQuestion)
        choices = models.CharField(max_length=200)
        votes  = models.IntegerField(default=0)

        def __unicode__(self):
                return self.choices

class PreTestUser(models.Model):
        pretestuser_num = models.IntegerField(default=1)
        first_question = models.ForeignKey(PreTestAnswer, related_name = 'pretestuser_firstquestion')
        second_question = models.ForeignKey(PreTestAnswer, related_name = 'pretestuser_secondquestion')
        
class PostTestQuestion(models.Model):
	question = models.CharField(max_length=200)
	question_number = models.IntegerField(default=1)
	isTextField = models.BooleanField()
	
	def __unicode__(self):
		return self.question
	
class PostTestAnswer(models.Model):
	question = models.ForeignKey(PostTestQuestion)
	choices = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __unicode__(self):
		return self.choices



class PostTestUser(models.Model):
        posttestuser_num = models.IntegerField(default=1)
        question_one = models.ForeignKey(PostTestAnswer, related_name = 'ppsttestuser_questionone')
        question_two = models.ForeignKey(PostTestAnswer, related_name = 'posttestuser_questiontwo')
        question_three = models.ForeignKey(PostTestAnswer, related_name = 'posttestuser_questionthree')
        question_four = models.ForeignKey(PostTestAnswer, related_name = 'posttestuser_questionfour')
        question_five = models.ForeignKey(PostTestAnswer, related_name = 'posttestuser_questionfive')
        question_six = models.ForeignKey(PostTestAnswer, related_name = 'posttestuser_questionsix')
        question_seven = models.ForeignKey(PostTestAnswer, related_name = 'posttestuser_questionseven')
        question_eight = models.ForeignKey(PostTestAnswer, related_name = 'posttestuser_questioneight')


