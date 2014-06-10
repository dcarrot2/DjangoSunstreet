from django.shortcuts import render
from django.shortcuts import get_object_or_404, get_list_or_404
from botvin_lifeskills.models import Question, Answer, Botvin_Section, User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.

def botvinSection(request, section, school_level):
            #We get the first two questions individually given
        #that they require a text field for response
    print "section: ", section
    print "school level", school_level
    questions = []
    for question in Question.objects.get_queryset().filter(section_letter = section).filter(school_level = school_level):
        questions.append(question)


    context = {}
    # for i in range(0, len(questions)):
    #     context["question_"+ str(i+1)] = questions[i]
    #
    # print questions
    context["questions"] = questions
    context["section"] = section
    context["school_level"] = school_level

    print "printing the context", context
    return render(request, "botvin/displayquestions.html", context)

def botvinSectionVote(request):#, section, school_level):
    questions = []
    # print "123456789"
    # print "request.post['1']", request.POST['1']
    # print "\n\n"
    # print "Should be the answer object: ", Answer.objects.get(pk=1).votes, "\n\n"

    print request
    questions = get_list_or_404(Question, section_letter = request.POST['section'], school_level = request.POST['school_level'])
    # print questions[0].answer_set.all()
    try:
        print "1"
        responses = []
        print "2"
        for i in range(0,len(questions)):
            print i
            print(Answer.objects.get(pk=request.POST["choice"+str(i+1)]))
            responses.append(Answer.objects.get(pk = request.POST["choice"+str(i+1)]))
        print responses
    except (KeyError, Question.DoesNotExist):
        print("Check your code")

        return render(request, 'botvin/displayquestions.html', {
		'error_message': "You forgot to select one or more choices."})


    return HttpResponseRedirect('botvin_lifeskills:botvinSection', args=['/botvin/section/',"B", "HS"])

def results(request):
    print "123456"
    return HttpResponse("Hello World")
