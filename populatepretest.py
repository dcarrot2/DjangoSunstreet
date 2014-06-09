import os

def populate():
    #list to make question objects
    prequestionlist = ["Which of the following best describes your interest in taking this LST class: (check one)",
                       "Which best describes how much you have been involved in gang activity over the last 30 days: (check one)"]

    #list that will eventually hold the question objects. Needed to populate answers with their specific questions
    questionobjectlist = []
    
    #list to make answer objects
    preanswerlist = ["Very interested", "Somewhat interested", "Not too interested", "Not at all interested",
                      "Very involved", "Somewhat involved", "Not too involved", "Not at all involved"]

    #Make PreTestAnswer objects from the questions
    for i in range(0, len(prequestionlist)):
        add_question(question=prequestionlist[i], question_number = i+1)

    #Make a list of type PreTestQuestions -- necessary to link answers to each question
    for question in PreTestQuestion.objects.all():
        questionobjectlist.append(question)

    #Add answers to PreTestQuestions
    for j in range(0, 4):
        add_answer(questionobjectlist[0],preanswerlist[j])

    for l in range(4, len(preanswerlist)):
        add_answer(questionobjectlist[1], preanswerlist[l])


    for q in PreTestQuestion.objects.all():
        for a in PreTestAnswer.objects.filter(question=q):
            print "-{0} - {1}".format(str(q), str(a))

#function to create PreTestQuestion objects
def add_question(question, question_number):
    p = PreTestQuestion.objects.get_or_create(question=question, question_number=question_number)[0]
    return p

#function to create PreTestAnswer objects
def add_answer(question, choices, votes=0):
    c = PreTestAnswer.objects.get_or_create(question=question, choices=choices, votes=votes)[0]
    return c

if __name__ == '__main__':
    print "Inscribing pre test questions into database..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', "sunstreet.settings")
    from lifeskills.models import PreTestQuestion
    from lifeskills.models import PreTestAnswer
    populate()



    

    

    
