from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from botvin_lifeskills.models import Question, Answer, Botvin_User_Run, School, User, Botvin_User_Final
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
import json
import datetime
import urllib2
import xlwt
import uuid
# Create your views here.


def temp(request):
    print datetime.datetime.now()
    return render(request, "botvin/temp.html")


def excel(request, school_level):
    users_1 = Botvin_User_Final.objects.get_queryset().filter(school_level=school_level)
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Botvin'+school_level+'.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("BotvinHighSchool")
    row_num = 0

    columns = [
            (u"Date Taken", 6000),
            (u'Student ID', 6000),
            (u"School ID", 6000),
            (u"School Level", 8000),

               ]

    for q in Question.objects.get_queryset().filter(school_level=school_level):
        columns.append((q.question, 8000))

    print "Col: ", columns

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    #For styling columns
    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        ws.col(col_num).width = columns[col_num][1]
        ws.col(col_num).width = columns[col_num][1]


    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    userList_row = 0

    for obj in users_1:

        row_num += 1

        #Write the student's student code, school code and school level into the spreadsheet
        ws.write(row_num, 0, str(obj.date_taken))
        ws.write(row_num,1,str(obj.user_key))
        ws.write(row_num,2,str(obj.school))
        ws.write(row_num, 3, school_level)
        col_num = 4;
        #We cycle through each column starting at the third column and we fill them with the responses of the student
        for answer in obj.answer_set.all():
            #ws.write(row_num, col_num, userList[col_num], font_style)
            ws.write(row_num, col_num, answer.choices)
            col_num += 1
        #Increment the index to move to next student's list
        userList_row += 1

            # set column width

    wb.save(response)
    return response



def botvinSection(request, section, school_level):
    try:
        if(section == 'A'):
            school = request.POST["School_Choice"]
            sessionID = request.COOKIES['hex']
            Botvin_User_Run.objects.get_or_create(school=school, user_key=sessionID, school_level=school_level)
            if(school == ""):
                print "Raising exception"
                raise Exception()

            school = urllib2.url2pathname(school)
    except:
        print "Exception. Did not choose a school"
        context = {}
        context["schools"] = School.objects.get_queryset()
        return render(request,"botvin/index.html", context)

    print "section: ", section
    print "school level", school_level
    questions = []
    for question in Question.objects.get_queryset().filter(section_letter = section).filter(school_level = school_level):
        questions.append(question)


    context = {}
    context["questions"] = questions
    context["section"] = section
    context["school_level"] = school_level

    #print "printing the context", context
    return render(request, "botvin/displayquestions.html", context)

def botvinSectionVote(request):#, section, school_level):
    questions = []
    sessionID = request.COOKIES['hex']
    current_section = request.POST["section"]
    following_section = ""
    school_level = request.POST['school_level']
    questions = get_list_or_404(Question, section_letter = current_section, school_level = school_level)
    try:
        run = Botvin_User_Run.objects.get_or_create(user_key = sessionID)
        run = run[0]
        print "run: ", run
        print "run type: ", type(run)
        for i in range(0,len(questions)):
            run.answer_set.add(Answer.objects.get(pk = request.POST["choice"+str(i+1)]))

    except (KeyError, Question.DoesNotExist):
        print("Check your code")

        return render(request, 'botvin/displayquestions.html', {
        'error_message': "You forgot to select one or more choices."})

    #We render surveys depending on the section
    if (current_section == "A"):
        following_section = "B"
    elif(current_section == "B"):
        following_section = "C"
    elif(current_section == "C"):
        following_section = "D"
    else:
        final = Botvin_User_Final.objects.get_or_create(user_key=run.user_key, school=run.school, date_taken=timezone.now(),
                                                        school_level = run.school_level)
        final=final[0]
        for ans in run.answer_set.all():
            final.answer_set.add(ans)
        run.delete()
        
        return redirect('botvin/thankyou')

    return redirect('/botvin/section/'+following_section+'/'+school_level)

def index(request):
    schools = School.objects.get_queryset()
    context = {}
    context["schools"] = schools
    response = HttpResponse()
    response = render(request, "botvin/index.html", context)
    hex = uuid.uuid1().hex
    response.set_cookie('hex', hex)
    return response

def end(request):
    
    return render(request,"botvin/end.html")


def results(request):
    print "123456"
    return HttpResponse("Hello World")