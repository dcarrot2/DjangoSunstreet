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
    for i in range(0, len(questions)):
        context["question_"+ str(i+1)] = questions[i]
    print context


    return render(request, "lifeskills/prequestions.html", context)
