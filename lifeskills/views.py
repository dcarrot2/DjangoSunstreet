from django.shortcuts import render
from django.shortcuts import get_object_or_404
from lifeskills.models import PreTestQuestion, PreTestAnswer, PreTestUser, PostTestQuestion, PostTestAnswer, PostTestUser
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

#Load each question individually? 

numOfPreUser = 1
numOfPostUser = 1

def pretest(request):
        #Get the two questions from the pretest survey
        first_question = PreTestQuestion.objects.get(question_number = 1)
        second_question = PreTestQuestion.objects.get(question_number = 2)

        context = {"first_question": first_question,
                   "second_question": second_question}

        return render(request, "lifeskills/prequestions.html", context)

def pretestvote(request):
        global numOfPreUser
        userCount = 1

        first = get_object_or_404(PreTestQuestion, question_number=1)
        second = get_object_or_404(PreTestQuestion, question_number=2)

        try:
                choiceFirst = first.pretestanswer_set.get(pk=request.POST['choice1'])
                choiceSecond = second.pretestanswer_set.get(pk=request.POST['choice2'])

                print 'First choice: ', choiceFirst
                print 'Second choice: ', choiceSecond

        except (KeyError, PreTestQuestion.DoesNotExist):
		print("Check your code")

		return render(request, 'lifeskills/prequestions.html', {
		'error_message': "You forgot to select one or more choices.",
		"first_question": first, "second_question": second})

	else:
                newUser = PreTestUser(pretestuser_num=numOfPreUser, first_question=choiceFirst,
                                     second_question=choiceSecond)
                print "Response received"

                choiceFirst.votes += 1
                choiceSecond.votes += 2

                newUser.save()
                choiceFirst.save()
                choiceSecond.save()
                numOfPreUser += 1

                return HttpResponseRedirect(reverse('lifeskills:response'))

def posttest(request):
        
        #We get the first two questions individually given
        #that they require a text field for response

        questions = []

        for question in PostTestQuestion.objects.all():
                questions.append(question)
        context = {}

        for i in range(len(questions)):
                context["question_" + str(i+1)] = questions[i]

	return render(request, "lifeskills/postquestions.html", context)


def posttestvote(request):
        global numOfPostUser
	userCount = 1
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
		
		choiceFirst = PostTestAnswer.objects.get_or_create(question=first, choices=firstTextResponse, votes=0)[0]
                choiceSecond = PostTestAnswer.objects.get_or_create(question=second, choices=secondTextResponse, votes=0)[0]
		choiceThird = third.posttestanswer_set.get(pk=request.POST['choice3'])
		choiceFourth = fourth.posttestanswer_set.get(pk=request.POST['choice4'])
		choiceFifth = fifth.posttestanswer_set.get(pk=request.POST['choice5'])
		choiceSixth = sixth.posttestanswer_set.get(pk=request.POST['choice6'])
		choiceSeventh = seventh.posttestanswer_set.get(pk=request.POST['choice7'])
		choiceEighth = eighth.posttestanswer_set.get(pk=request.POST['choice8'])	
		
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
		newUser = PostTestUser(posttestuser_num=numOfPostUser, question_one=choiceFirst,
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

                numOfPostUser+=1

		return HttpResponseRedirect(reverse('lifeskills:response'))

def response(request):

	return render(request, 'lifeskills/response.html')

	
