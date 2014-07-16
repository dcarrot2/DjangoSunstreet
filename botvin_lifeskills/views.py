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

responses = {}
school_user = {}

def temp(request):
    print datetime.datetime.now()
    return render(request, "botvin/temp.html")


def excel(request):
    import xlwt
    Users = User.objects.all()
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=BotvinHighSchool.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("BotvinHighSchool")

    userList = []
    row_num = 0

    numUsers = len(User.objects.get_queryset().filter(school_level="HS"))
    jsonDec = json.decoder.JSONDecoder()

    columns = [
            (u"Date Taken", 6000),
            (u"Student ID", 6000),
            (u"School ID", 6000),
            (u"School Level", 8000),

               ]

    for question in range(3,54):
        columns.append(("Q"+str(question-2), 8000))

    print "Col: ", columns

    for user in User.objects.get_queryset().filter(school_level = "HS"):
        userList.append(jsonDec.decode(user.myList))

    print "\n\nMy User List: ", userList


    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    #For styling columns
    for col_num in xrange(len(columns)):
        ws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column widthws.write(row_num, col_num, columns[col_num][0], font_style)
        # set column width
        ws.col(col_num).width = columns[col_num][1]
        ws.col(col_num).width = columns[col_num][1]


    font_style = xlwt.XFStyle()
    font_style.alignment.wrap = 1

    userList_row = 0

    for obj in User.objects.get_queryset().filter(school_level="HS"):

        row_num += 1

        #Write the student's student code, school code and school level into the spreadsheet
        ws.write(row_num, 0, obj.date_survey_taken)
        ws.write(row_num,1,obj.school_code)
        ws.write(row_num,2,obj.school_level)

        #We cycle through each column starting at the third column and we fill them with the responses of the student
        for col_num in xrange(51):
            #ws.write(row_num, col_num, userList[col_num], font_style)
            ws.write(row_num, col_num + 3, userList[userList_row][col_num])

        #Increment the index to move to next student's list
        userList_row += 1

            # set column width

    wb.save(response)
    return response



def botvinSection(request, section, school_level):
    try:
        #print "School: ", request.COOKIES["school"]
        if(section == 'A'):
            school = request.POST["School_Choice"]
            sessionID = request.COOKIES['hex']
            Botvin_User_Run.objects.get_or_create(school=school, user_key=sessionID)
            #print "School after assignment: ", school
            if(school == ""):
                print "Raising exception"
                raise Exception()

            school = urllib2.url2pathname(school)
        #print "School with %20 replaced: ", school

        #print "SessionID: ", sessionID
        #school_user[request.COOKIES["csrftoken"]] = school


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
    # for i in range(0, len(questions)):
    #     context["question_"+ str(i+1)] = questions[i]
    #
    # print questions
    context["questions"] = questions
    context["section"] = section
    context["school_level"] = school_level

    #print "printing the context", context
    return render(request, "botvin/displayquestions.html", context)

def botvinSectionVote(request):#, section, school_level):
    questions = []
    # print "123456789"
    # print "request.post['1']", request.POST['1']
    # print "\n\n"
    # print "Should be the answer object: ", Answer.objects.get(pk=1).votes, "\n\n"

    #print "Request: ", request
    sessionID = request.COOKIES['hex']
    current_section = request.POST["section"]
    following_section = ""
    school_level = request.POST['school_level']
    # print request
    questions = get_list_or_404(Question, section_letter = current_section, school_level = school_level)
    # print questions[0].answer_set.all()
    try:
        #print "1"
        run = Botvin_User_Run.objects.get_or_create(user_key = sessionID)
        run = run[0]
        print "run: ", run
        print "run type: ", type(run)
        for i in range(0,len(questions)):
            #print i

            run.answer_set.add(Answer.objects.get(pk = request.POST["choice"+str(i+1)]))
        #print responses
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
        final = Botvin_User_Final.objects.get_or_create(user_key=run.user_key, school=run.school, date_taken=timezone.now())
        final=final[0]
        for ans in run.answer_set.all():
            final.answer_set.add(ans)
        run.delete()

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


def results(request):
    print "123456"
    return HttpResponse("Hello World")