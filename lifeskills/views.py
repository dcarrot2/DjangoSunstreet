from django.shortcuts import render
from lifeskills.models import Question, Answer
# Create your views here.

#Load each question individually? 

def pretest(request):
        #We get the first two questions individually given
        #that they require a text field for response
        first_question = Question.objects.get(pk=1)
        second_question = Question.objects.get(pk=3)
	pre_questions = Question.objects.order_by('pub_date')[2:8]

	for x in pre_questions:
		print x

	context = {"pre_questions": pre_questions, "first_question": first_question, "second_question": second_question}

	return render(request, "lifeskills/prequestions.html", context)

	
