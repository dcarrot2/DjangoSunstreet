from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, get_list_or_404
from botvin_lifeskills.models import Question, Answer, Botvin_Section, User
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.utils import timezone
from django_excel_templates import *
from django_excel_templates.color_converter import *
import json
import datetime
import xlwt
# Create your views here.

responses = []

def temp(request):
    print datetime.datetime.now()
    return render(request, "botvin/temp.html")


def excel(request):
   
    Users = User.objects.all()
    import xlwt
    response = HttpResponse(mimetype='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=mymodel.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet("MyModel")
    
    userList = [[]]
    row_num = 0
    
    numUsers = len(User.objects.get_queryset().filter(school_level="HS"))
    jsonDec = json.decoder.JSONDecoder()
    
    columns = [
            (u"Student ID", 2000),
            (u"School ID", 6000),
            (u"School Level", 8000),   
               
               ]
    
    for question in range(3,54):
        columns.append(("Q"+str(question-2), 8000))
        
    print "Col: ", columns
    
    for user in User.objects.get_queryset().filter(school_level = "HS"):
        userList.append(jsonDec.decode(user.myList))
    
    
   
    
    #for question in xrange(len(columns)):
        
    
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
    
    for obj in User.objects.get_queryset().filter(school_level="HS"):
        
        row_num += 1
        
        row = [
               obj.student_code,
               obj.school_code]
        
        for col_num in xrange(len(userList)):
            
            ws.write(row_num, col_num+3, userList[row_num][col_num], font_style)
            # set column width
    
    wb.save(response)
    return response
        
   
    
  #=============================================================================
  #   formatter = ExcelFormatter()
  #   simpleStyle = ExcelStyle(vert=2, wrap=1)
  #   formatter.addBodyStyle(simpleStyle)
  #   formatter.setWidth('name, category, publish_date,bought_on', 3000)
  #   formatter.setWidth('price', 600)
  #   formatter.setWidth('ebook', 1200)
  #   formatter.setWidth('about', 20000)
  #   
  # 
  #   
  #   simple_report = ExcelReport()
  #   simple_report.addSheet("TestSimple")
  #   #filter = ExcelFilter(order='name, category, publish_date, about, bought_on, price, ebook')
  #   simple_report.addQuerySet(Users, REPORT_HORZ, formatter)
  #   
  #   response = HttpResponse(simple_report.writeReport(), mimetype='application/ms-excel')
  #   response['Content-Disposition'] = 'attachment; filename=simple_text.xls'
  #   print 'LOL'
  #   return response
  #=============================================================================



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
    current_section = request.POST["section"]
    following_section = ""
    school_level = request.POST['school_level']
    # print request
    questions = get_list_or_404(Question, section_letter = current_section, school_level = school_level)
    # print questions[0].answer_set.all()
    try:
        print "1"
        global responses
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
    
    #We render surveys depending on the section
    if (current_section == "A"):
        following_section = "B"
    elif(current_section == "B"):
        following_section = "C"
    elif(current_section == "C"):
        following_section = "D"
    else:
        #typecast reponses from Answer to String objects before making json dump into User.myList textfield    
        for x in range(len(responses)):
            responses[x] = str(responses[x])
        
        print "Length of responses: ", len(responses)
        print responses
        r = User(student_code=1, school_code=2, myList = json.dumps(responses), num_questions_answered = len(responses), school_level=school_level)
        r.save()
        User.objects.all()
        
            
        
        
        responses = []

    return redirect('/botvin/section/'+following_section+'/'+school_level)


def results(request):
    print "123456"
    return HttpResponse("Hello World")
