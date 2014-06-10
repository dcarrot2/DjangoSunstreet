import os
def populate():
    #high school questionnaire will use the eighth index of this question list
    sectionAQuestions = ["My age", "Are you:", "Who do you live with most of the time? (Pick only one)", "Are you Hispanic or Latino?",
                        "What is your race? (SELECT ONE OR MORE.)", "What grade are you in?", "7. What grades do you generally get in school? (Pick only one)",
                        "About how many days were you absent from school last year? (Pick only one)","Do you currently have a job? (Pick only one)"]

    hsSectionBQuestions = ["Setting a health goal is a good way to try to improve your health.", "Paying attention to your health is not important when you are at my age.",
                          "My health is not impacted by my day-to-day decisions.", "Having a positive attitude can help you make decisions more effectively.",
                          "Your risk-taking is impacted by your drug or alcohol use.", "Once you have done something risky and nothing bad happens, it is less risky next time you do it.",
                          "A persons culture is shaped by the media.", "There is nothing I can do to know if media messages are accurate.",
                          "Stress and anger do not really impact other emotions.", "People handle an emotional trigger the same way.",
                          "Effective communication is being able to say everything on your mind.","There is a difference between misunderstandings and disagreements.",
                          "Your health is not really affected by your relationships with others.","Asserting yourself means standing up for yourself while simultaneously respecting the rights of others."]

    hsSectionCQuestions = ["Peers my age who drink alcohol are more grown-up.","Smoking marijuana makes you look cool.","Smoking cigarettes makes you look cool.",
                          "Peers my age who smoke marijuana are more grown-up.", "Peers my age who drink alcohol have more friends.",
                          "Peers my age who smoke have more friends.","Smoking marijuana lets you have more fun.","Drinking alcohol makes you look cool.",
                          "Peers my age who use cocaine or other drugs have more friends.", "Peers my age who use cocaine or other drugs are more grown-up.",
                          "Smoking cigarettes lets you have more fun.", "Peers my age who smoke cigarettes are more grown-up.", "Using cocaine or other drugs lets you have more fun.",
                          "Using cocaine or other drugs makes you look cool.","Drinking alcohol lets you have more fun.","Peers my age who use marijuana have more friends."]

    hsSectionDQuestions = ['...say no when someone offers you a cigarette?','...say no when someone offers you marijuana or hashish?','...say no when someone offers you beer, wine, or liquor?','...say no when someone offers you cocaine or other drugs?',
                          '...say no when someone offers you glue, paint, gas, or other things you inhale to get high?',"Tell someone if they give you less change (money) than you're supposed to get back after you pay for something",
                          'Say no to someone who asks to borrow money from you',"Tell someone to go to the end of the line if they try to cut in line ahead of you",
                          "Relax all the muscles in your body","Breathe in slowly while you count to four then hold your breath for four and breathe out for a count of four",
                          "If you find that something is really difficult, you get frustrated and quit", "You stick to what you are doing until you are finished with it"]

    msSectionBQuestions = ["Most adults smoke cigarettes.","Smoking a cigarette causes your heart to beat slower.","Few adults drink wine, beer, or liquor everyday.",
                           "Most people my age smoke marijuana.","Smoking marijuana causes your heart to beat faster.","Most adults use cocaine or other hard drugs.",
                           "Cocaine and other hard drugs always make you feel good.", "What we believe about ourselves affects the way we act or behave.",
                           "It is almost impossible to develop a more positive self-image.","It is important to measure how far you have come toward reaching your goal.",
                           "It is a good idea to make a decision and then think about the consequences later.","Smoking can affect the steadiness of your hands.",
                           "A stimulant is a chemical that calms down the body.", "Smoking reduces a persons endurance for physical activity.",
                           "A serving of beer or wine contains less alcohol than a serving of hard liquor such as whiskey.",
                           "Alcohol is a depressant.","Marijuana smoking can improve your eyesight.","Some advertisers are deliberately deceptive.",
                           "Companies advertise only because they want you to have all the facts about their product.", "It is a good idea to get all information about a product from its ads.",
                           "Most people do not experience anxiety.", "There is very little you can do when you feel anxious.","Deep breathing is one way to lessen anxiety.",
                           "Mental rehearsal is a poor relaxation technique.", "You can avoid misunderstandings by assuming the other person knows what you mean.",
                           "Effective communication is when both sender and receiver interpret a message in the same way.", "Relaxation techniques are of no use when meeting people.",
                           "A compliment is more effective when it is said sincerely.", "A nice way of ending a conversation is to tell the person you enjoyed talking with him/her.",
                           "Sense of humor is an example of a non-physical attribute.", "It is better to be polite and lead someone on, even if you do not want to go out with them.",
                           "Almost all people who are assertive are either rude or hostile."]

    msSectionCQuestions = ["Kids who drink alcohol are more grown-up.", "Smoking cigarettes makes you look cool.","Kids who drink alcohol have more friends.",
                           "Kids who smoke have more friends.","Drinking alcohol makes you look cool.","Smoking cigarettes lets you have more fun.", "Kids who smoke cigarettes are more grown-up.",
                           "Drinking alcohol lets you have more fun."]

    msSectionDQuestions = ["Say no when someone tries to get you to smoke a cigarette?"," Say no when someone tries to get you to drink beer, wine, or liquor?",
                           "Say no when someone tries to get you to smoke marijuana or hashish?","Say no when someone tries to get you to use cocaine or other drugs?",
                           "Say no when someone tries to get you to sniff glue, paint, gas, or other things you inhale to get high?",
                           "Tell someone if they give you less change (money) than you're supposed to get back after you pay for something.",
                           "Say no to someone who asks to borrow money from you.","Tell someone to go to the end of the line if they try to cut in line ahead of you.",
                           "Relax all the muscles in your body, starting with your feet and legs.", "Breathe in slowly while you count to four and hold your breath for four and breathe out for a count of four.",
                           "If you find that something is really difficult, you get frustrated and quit.","You stick to what you are doing until you are finished with it."]
    esSectionBQuestions = ["Cigarette smoking can cause your skin to wrinkle.", "Cigarette smoking can cause your teeth to turn yellow or brown.","Cigarette smoking causes your heart to beat faster.",
                           "Smoking cigarettes can cause mouth cancer.","People who smoke cigarettes can usually stop anytime they want.","Most teenagers smoke cigarettes.",
                           "Most adults smoke cigarettes.","It is always best to make decisions quickly.","You should always let other people influence your decisions.",
                           "Advertisements are always true.", "Stress can cause you to get sick.", "When you feel stressed, there is nothing you can do to stop it.",
                           "Even if someone does not say anything, we can tell how they are feeling by the way they move their body.",
                           "A good way to refuse to do something is to be assertive.","Beginning your sentences with the word I is a good way to be assertive.",
                           'Peer pressure means that an adult tries to get you to do something you do not want to do.',"There is nothing you can do about peer pressure except go along with it.",
                           "When we feel bad about ourselves, it affects how well we do in school, sports or other activities."]
    esSectionCQuestions = ["Kids who smoke cigarettes have more fun than non- smokers.", "Kids who smoke cigarettes have more friends than non-smokers.",
                           "Kids who smoke cigarettes look more grown-up than non-smokers.", "Kids who drink alcohol (beer, wine, or liquor) have more fun than non-drinkers.",
                           "Kids who drink alcohol (beer, wine, or liquor) have more friends than non-drinkers.","Kids who drink alcohol (beer, wine, or liquor) look more grown-up than non-drinkers.",
                           "Since a lot of people smoke cigarettes, it cannot be that bad for you.","Since a lot of people drink alcohol, it cannot be that bad for you.",
                           ]
    esSectionDQuestion = ["When you need to make a decision, how often do you think about your choices and what will happen?",
                          "When you see or hear an ad on TV or the radio, how often do you remember that ads might not be telling the truth?",
                          "When you feel nervous or stressed out, how often do you take deep breaths to relax?","When you feel nervous or stressed out, how often do you imagine something in your head to relax?",
                          "When you want to communicate with someone better, how often do you try to say things that are clear and easy to understand?",
                          "How often do you ask questions when you do not understand something?","How likely would you be to tell someone to move if they cut ahead of you in line?",
                          "How likely would you be to say hello to someone you do not know well?"]

    sectionAQuestion1Answers = ["14","15","16","17","18","19","20","21"]
    sectionAQuestion2Answers = ["Male","Female"]
    sectionAQuestion3Answers = ["Mother and father", "Only mother", "Mother and stepfather","Only father","Stepmother and father",
                                "Some with mother/some with father", "Other relative","Guardian or foster parent","Alone or with friends"]
    sectionAQuestion4Answers = ["Yes", "No"]
    sectionAQuestion5Answers = ["American Indian/Alaska Native","Asian","Native Hawaiian or Other Pacific Islander","Black or African American","White"]
    sectionAQuestion6Answers = ["3rd grade","4th grade","5th grade","6th grade","7th grade","8th grade","9th grade","9th grade","10th grade","11th grade","12th grade"]
    sectionAQuestion7Answers = ["Mostly As (90-100)","Mostly Bs (80-89)","Mostly Cs (70-79)","Mostly Ds (60-69)","Ds or lower (less than 60)"]
    sectionAQuestion8Answers = ["None","1-2 days","3-6 days","7-15 days","16 or more days"]
    sectionAQuestion9Answers = ["I am not currently employed","Yes, I usually work less than 10 hours per week","Yes, I usually work from 10 to 20 hours per week","Yes, I usually work more than 20 hours per week"]
    sectionBAnswers = ["True","False"]
    #section C and D answers are the same for the elementary school students
    sectionCandDElementaryAnswers = ["Never", "Sometimes", "Most of the Time"]
    sectionCAnswers = ["Strongly Disagree","Disagree","Neither Agree Nor Disagree","Agree","Strongly Agree"]
    sectionDAnswers = ["Definitely Would","Probably Would","Not Sure","Probably Would Not", "Definitely Would Not"]
    sectionDAnswersHS910 = ["Never", "Almost Never", "Sometimes", "Almost Always", "Always"]
    #question 11 and 12 need the answers for section C for high school and middle school

    schoolList = ["HS", "MS", "ES"]
    sectionID = ["A","B","C","D"]

    for school in schoolList:
        for section in sectionID:
            Botvin_Section.objects.get_or_create(section_letter = section, school_level = school)



    for i in range(0,len(sectionAQuestions)):

        if (i == 0):
            add_question(sectionAQuestions[i], i+1, "A", "HS")
            for x in sectionAQuestion1Answers:
                add_answer(Question.objects.get(question_number = 1), x)
        if(i == 1):
            add_question(sectionAQuestions[i], i+1, "A","HS")
            for x in sectionAQuestion2Answers:
                add_answer(Question.objects.get(question_number = 2), x)
        if(i == 2):
            add_question(sectionAQuestions[i], i+1, "A", "HS")
            for x in sectionAQuestion3Answers:
                add_answer(Question.objects.get(question_number = 3), x)
        if(i==3):
            add_question(sectionAQuestions[i], i+1, "A", "HS")
            for x in sectionAQuestion4Answers:
                add_answer(Question.objects.get(question_number = 4), x)
        if(i == 4):
            add_question(sectionAQuestions[i], i+1, "A", "HS")
            for x in sectionAQuestion5Answers:
                add_answer(Question.objects.get(question_number = 5), x)
        if(i == 5):
            add_question(sectionAQuestions[i], i+1, "A", "HS")
            for x in sectionAQuestion6Answers:
                add_answer(Question.objects.get(question_number = 6), x)
        if(i == 6):
            add_question(sectionAQuestions[i], i+1, "A", "HS")
            for x in sectionAQuestion7Answers:
                add_answer(Question.objects.get(question_number = 7), x)
        if(i == 7):
            add_question(sectionAQuestions[i], i+1, "A", "HS")
            for x in sectionAQuestion8Answers:
                add_answer(Question.objects.get(question_number = 8), x)
        if(i == 8):
            add_question(sectionAQuestions[i], i+1, "A", "HS")
            for x in sectionAQuestion9Answers:
                add_answer(Question.objects.get(question_number = 9), x)

    organizeSection(hsSectionBQuestions, "B", "HS", sectionBAnswers)
    organizeSection(msSectionBQuestions, "B", "MS", sectionBAnswers)
    organizeSection(esSectionBQuestions, "B", "ES", sectionBAnswers)
    organizeSection(hsSectionCQuestions, "C", "HS", sectionCAnswers)
    organizeSection(msSectionCQuestions, "C", "MS", sectionCAnswers)
    organizeSection(esSectionCQuestions, "C", "ES", sectionCandDElementaryAnswers)

    for i in range(0, len(hsSectionDQuestions)):
        if (i <=7):
            add_question(hsSectionDQuestions[i], i+1, "D", "HS")
            for x in sectionDAnswers:
                add_answer(Question.objects.get(question_number=i+1, section_letter="D", school_level="HS"),x)
        if(i > 7 and i < 10):
            add_question(hsSectionDQuestions[i], i+1, "D", "HS")
            for x in sectionDAnswersHS910:
                add_answer(Question.objects.get(question_number=i+1, section_letter="D", school_level = "HS"),x)
        if(i >= 10):
            add_question(hsSectionDQuestions[i], i+1, "D", "HS")
            for x in sectionCAnswers:
                add_answer(Question.objects.get(question_number=i+1, section_letter="D", school_level="HS"),x)

    for i in range(0, len(msSectionDQuestions)):
        if(i<10):
            add_question(msSectionDQuestions[i], i+1, "D","MS")
            for x in sectionDAnswers:
                add_answer(Question.objects.get(question_number=i+1, section_letter="D", school_level="MS"),x)
        if (i>=10):
            add_question(msSectionDQuestions[i], i+1, "D", "MS")
            for x in sectionCAnswers:
                add_answer(Question.objects.get(question_number=i+1, section_letter="D", school_level="MS"), x)

    organizeSection(esSectionDQuestion, "D", "ES", sectionCandDElementaryAnswers)

def add_answer(question, choices):
    votes = 0
    c = Answer.objects.get_or_create(answer=question, choices=choices, votes=votes)[0]
    return c

def add_question(q, q_num, sect, level):
    q = Question.objects.get_or_create(question = q,question_number= q_num,
                                       section=Botvin_Section.objects.get_queryset().
                                       filter(section_letter = sect).filter(school_level=level)[0],
                                       school_level = level, section_letter = sect)
    return q

def organizeSection(questionSet, lifeskillsSection, schoolLevel, answerSet):
    for i in range(0, len(questionSet)):
        add_question(questionSet[i], i+1, lifeskillsSection, schoolLevel)
        for x in answerSet:
            add_answer(Question.objects.get(question_number = i+1, section_letter=lifeskillsSection, school_level=schoolLevel), x)
    return

if __name__ == '__main__':
    print "Inscribing questions into database..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',"sunstreet.settings")
    from botvin_lifeskills.models import Question, Answer, Botvin_Section
    populate()