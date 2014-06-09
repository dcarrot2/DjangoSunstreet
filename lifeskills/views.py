from django.shortcuts import render
from django.shortcuts import get_object_or_404
from lifeskills.models import PreTestQuestion, PreTestAnswer, PreTestUser, PostTestQuestion, PostTestAnswer, PostTestUser
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

#Load each question individually? 

numOfUser = 1

def pretest(request):
        #Get the two questions from the pretest survey
        first_question = PreTestQuestion.objects.get(question_number = 1)
        second_question = PreTestQuestion.objects.get(question_number = 2)

        context = {"first_question": first_question,
                   "second_question": second_question}

        return render(request, "lifeskills/prequestions.html", context)

def posttest(request):
        #We get the first two questions individually given
        #that they require a text field for response

        questions = []

        for question in PostTestQuestion.objects.all():
                questions.append(question)
        context = {}

        for i in range(len(questions)):
                context["question_" + str(i+1)] = questions[i]
        
##        first_question = PostTestQuestion.objects.get(question_number = 1)
##        second_question = PostTestQuestion.objects.get(question_number = 2)
##        third_question = PostTestQuestion.objects.get(question_number = 3)
##        fourth_question = PostTestQuestion.objects.get(question_number = 4)
##        fifth_question = PostTestQuestion.objects.get(question_number = 5)
##        sixth_question = PostTestQuestion.objects.get(question_number = 6)
##        seventh_question = PostTestQuestion.objects.get(question_number = 7)
##        eighth_question = PostTestQuestion.objects.get(question_number = 8)
##
##	context = {"first_question": first_question,
##                   "second_question": second_question, "third_question": third_question,
##                   "fourth_question": fourth_question, "fifth_question": fifth_question,
##                   "sixth_question": sixth_question, "seventh_question": seventh_question,
##                   "eighth_question": eighth_question}

	return render(request, "lifeskills/postquestions.html", context)


def posttestvote(request):
	userCount = 1;
	#get all question objects
	first = get_object_or_404(PostTestQuestion, question_number=1)
	second = get_object_or_404(PostTestQuestion, question_number=2)
	third = get_object_or_404(PostTestQuestion, question_number=3)
	fourth = get_object_or_404(PostTestQuestion, question_number=4)
	fifth = get_object_or_404(PostTestQuestion, question_number=5)
	sixth = get_object_or_404(PostTestQuestion, question_number=6)
	seventh = get_object_or_404(PostTestQuestion, question_number=7)
	eighth = get_object_or_404(PostTestQuestion, question_number=8)

	try:
		firstTextResponse = request.POST['textarea1']
		secondTextResponse = request.POST['textarea2']
		
		choiceFirst = PostTestAnswer.objects.get_or_create(answer=first, choices=firstTextResponse, votes=0)[0]
                choiceSecond = PostTestAnswer.objects.get_or_create(answer=second, choices=secondTextResponse, votes=0)[0]
		choiceThird = third.PostTestAnswer_set.get(pk=request.POST['choice3'])
		choiceFourth = fourth.PostTestAnswer_set.get(pk=request.POST['choice4'])
		choiceFifth = fifth.PostTestAnswer_set.get(pk=request.POST['choice5'])
		choiceSixth = sixth.PostTestAnswer_set.get(pk=request.POST['choice6'])
		choiceSeventh = seventh.PostTestAnswer_set.get(pk=request.POST['choice7'])
		choiceEighth = eighth.PostTestAnswer_set.get(pk=request.POST['choice8'])	
		
		print "First choice: ", choiceFirst
		print "Second choice: ", choiceSecond
		print "Third choice: ", choiceThird
		print "Fourth choice: ", choiceFourth
		print "Fifth choice: ", choiceFifth
		print "Sixth choice: ", choiceSixth
		print "Seventh choice: ", choiceSeventh
		print "Eighth choice: ", choiceEighth

	except (KeyError, PostTestQuestion.DoesNotExist):
		print("Check your code")

		return render(request, 'lifeskills/prequestions.html', {
		'error_message': "You forgot to select one or more choices.",
		"first_question": first, "second_question": second, "third_question": third,
		"fourth_question": fourth, "fifth_question": fifth, "sixth_question": sixth,
		"seventh_question": seventh, "eighth_question": eighth
		})
	
	else:
                
		
		newUser = PostTestUser(preuser_num=numOfUser, question_one=choiceFirst,
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

                numUser+=1

		return HttpResponseRedirect(reverse('lifeskills:response'))

def response(request):

	return render(request, 'lifeskills/response.html')

	
