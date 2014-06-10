from django.shortcuts import render
from django.shortcuts import get_object_or_404
from botvin_lifeskills.models import Question, Answer, Botvin_Section, User
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
# Create your views here.

def botvinSection(request, section, school_level):
            #We get the first two questions individually given
        #that they require a text field for response
    questions = []
    for question in Question.objects.get_queryset().filter(section_letter = section).filter(school_level = school_level):
        questions.append(question)


    context = {}
    # for i in range(0, len(questions)):
    #     context["question_"+ str(i+1)] = questions[i]
    #
    context["questions"] = questions
    context["section"] = section
    context["school_level"] = school_level
    print "Context: ", context
    return render(request, "botvin/displayquestions.html", context)

def botvinSectionVote(request, section, school_level):
    print "LOL"
    questions = []
    for question in Question.objects.get_queryset().filter(section_letter=section).filter(school_level=school_level):
        questions.append(question)
    try:
        responses = []
        for i in range(0,len(questions)):
            responses.append(Answer.objects.get(pk = request.POST['choice'+str(i+1)]))
        for i in range(0, len(responses)):
            print "Response " + str(i+1)+":" + responses[i]
    except (KeyError, Question.DoesNotExist):
        print("Check your code")

        return render(request, 'botvin/displayquestions.html', {
		'error_message': "You forgot to select one or more choices."})

    return HttpResponseRedirect(reverse('lifeskills:response'))

