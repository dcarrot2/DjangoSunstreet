from django.shortcuts import render
from django.shortcuts import get_object_or_404
from lifeskills.models import PreTestQuestion, PreTestAnswer, PreTestUser
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

#Load each question individually? 

numOfUser = 1

def pretest(request):
        #We get the first two questions individually given
        #that they require a text field for response
    questions=[]
    for question in PreTestQuestion.objects.get_queryset():
        questions.append(question)
        # first_question = PreTestQuestion.objects.get(question_number = 1)
        # second_question = PreTestQuestion.objects.get(question_number = 2)
        # third_question = PreTestQuestion.objects.get(question_number = 3)
        # fourth_question = PreTestQuestion.objects.get(question_number = 4)
        # fifth_question = PreTestQuestion.objects.get(question_number = 5)
        # sixth_question = PreTestQuestion.objects.get(question_number = 6)
        # seventh_question = PreTestQuestion.objects.get(question_number = 7)
        # eighth_question = PreTestQuestion.objects.get(question_number = 8)

	# context = {"first_question": first_question,
     #               "second_question": second_question, "third_question": third_question,
     #               "fourth_question": fourth_question, "fifth_question": fifth_question,
     #               "sixth_question": sixth_question, "seventh_question": seventh_question,
     #               "eighth_question": eighth_question}
    context = {}

    for i in range(len(questions)):
        context["question_"+str(i+1)] = questions[i]


	return render(request, "lifeskills/prequestions.html", context)


def pretestvote(request):
	userCount = 1
	#get all question objects
	first = get_object_or_404(PreTestQuestion, question_number=1)
	second = get_object_or_404(PreTestQuestion, question_number=2)
	third = get_object_or_404(PreTestQuestion, question_number=3)
	fourth = get_object_or_404(PreTestQuestion, question_number=4)
	fifth = get_object_or_404(PreTestQuestion, question_number=5)
	sixth = get_object_or_404(PreTestQuestion, question_number=6)
	seventh = get_object_or_404(PreTestQuestion, question_number=7)
	eighth = get_object_or_404(PreTestQuestion, question_number=8)

	try:
		firstTextResponse = request.POST['textarea1']
		secondTextResponse = request.POST['textarea2']
		
		choiceFirst = PreTestAnswer.objects.get_or_create(answer=first, choices=firstTextResponse, votes=0)[0]
                choiceSecond = PreTestAnswer.objects.get_or_create(answer=second, choices=secondTextResponse, votes=0)[0]
		choiceThird = third.pretestanswer_set.get(pk=request.POST['choice3'])
		choiceFourth = fourth.pretestanswer_set.get(pk=request.POST['choice4'])
		choiceFifth = fifth.pretestanswer_set.get(pk=request.POST['choice5'])
		choiceSixth = sixth.pretestanswer_set.get(pk=request.POST['choice6'])
		choiceSeventh = seventh.pretestanswer_set.get(pk=request.POST['choice7'])
		choiceEighth = eighth.pretestanswer_set.get(pk=request.POST['choice8'])	
		
		print "First choice: ", choiceFirst
		print "Second choice: ", choiceSecond
		print "Third choice: ", choiceThird
		print "Fourth choice: ", choiceFourth
		print "Fifth choice: ", choiceFifth
		print "Sixth choice: ", choiceSixth
		print "Seventh choice: ", choiceSeventh
		print "Eighth choice: ", choiceEighth

	except (KeyError, PreTestQuestion.DoesNotExist):
		print("Check your code")

		return render(request, 'lifeskills/prequestions.html', {
		'error_message': "You forgot to select one or more choices.",
		"first_question": first, "second_question": second, "third_question": third,
		"fourth_question": fourth, "fifth_question": fifth, "sixth_question": sixth,
		"seventh_question": seventh, "eighth_question": eighth
		})
	
	else:
                
		
		newUser = PreTestUser(preuser_num=numOfUser, question_one=choiceFirst,
                                      question_two=choiceSecond,question_three=choiceThird,
                                      question_four=choiceFourth, question_five=choiceFifth,
                                      question_six=choiceSixth, question_seven=choiceSeventh,
                                      question_eight=choiceEighth)

                print "First text: ", firstTextResponse

		print "pass"

		
		
		choiceThird.votes += 1
		choiceFourth.votes += 1
		choiceFifth.votes ++ 1
		choiceSixth.votes += 1
		choiceSeventh.votes += 1
		choiceEighth.votes += 1

                newUser.save()
                choiceThird.save()
                choiceFourth.save()
                choiceFifth.save()
                choiceSixth.save()
                choiceSeventh.save()
                choiceEighth.save()

		return HttpResponseRedirect(reverse('lifeskills:response'))

def response(request):

	return render(request, 'lifeskills/response.html')

	
