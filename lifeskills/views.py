from django.shortcuts import render
from lifeskills.models import PreTestQuestion, PreTestAnswer
# Create your views here.

#Load each question individually? 

def pretest(request):
        #We get the first two questions individually given
        #that they require a text field for response
        first_question = PreTestQuestion.objects.get(question_number = 1)
        second_question = PreTestQuestion.objects.get(question_number = 2)
        third_question = PreTestQuestion.objects.get(question_number = 3)
        fourth_question = PreTestQuestion.objects.get(question_number = 4)
        fifth_question = PreTestQuestion.objects.get(question_number = 5)
        sixth_question = PreTestQuestion.objects.get(question_number = 6)
        seventh_question = PreTestQuestion.objects.get(question_number = 7)
        eighth_question = PreTestQuestion.objects.get(question_number = 8)

	context = {"first_question": first_question,
                   "second_question": second_question, "third_question": third_question,
                   "fourth_question": fourth_question, "fifth_question": fifth_question,
                   "sixth_question": sixth_question, "seventh_question": seventh_question,
                   "eighth_question": eighth_question}

	return render(request, "lifeskills/prequestions.html", context)

	
