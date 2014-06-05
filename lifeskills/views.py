from django.shortcuts import render
from lifeskills.models import PreTestQuestion, PreTestAnswer
# Create your views here.

#Load each question individually? 

def pretest(request):
        #We get the first two questions individually given
        #that they require a text field for response
        first_question = PreTestQuestion.objects.get(question_number = 1)
        second_question = PreTestQuestion.objects.get(question_number = 2)
	pre_questions = PreTestQuestion.objects.all()

	for x in pre_questions:
		print x

	context = {"pre_questions": pre_questions, "first_question": first_question, "second_question": second_question}

	return render(request, "lifeskills/prequestions.html", context)

	
