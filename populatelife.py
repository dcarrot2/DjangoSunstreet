import os


def populate():
	#list to make question objects
	prequestionlist = ["What is the main thing you learned from the Life Skills training class?",
			"How has the class changed the way you act?",
			"Did you talk with your family or friends about what you learned in the class?", "Has the class changed the amount of alcohol or drugs you use?", "How likely are you to be involved in violent or 'risky' behavior now?","Which best describes how much you have been involved in gang activity over the last 30 days: (check one)", "Has the class changed your attitudes about gangs?","Overall, how important is this class to you life?"]
	
	#list that will eventually hold the question objects. Needed to populate answers with their 		specific questions
	questionobjectlist = []	

	#list to make answer objects
	preanswerlist = ["Yes","No","I drink/use about the same","I drink/use a little less now","I drink/use a lot less now","I don't drink/use at all now","Very likely","Somewhat likely","Not likely at all","Very involved","Somewhat involved","Not too involved","Not at all involved","I still think gangs are cool","I'm not so sure they're cool now","I don't think they're cool at all now","Very important,","Kind of important","Not very important"]
	
	#run through list and add to database
	for i in range(0, len(prequestionlist)):
		add_question(question=prequestionlist[i], question_number= i+1)

	#print questions to screen
	for q in PreTestQuestion.objects.all():
		print str(q)
	
	#get objects and append to empty list
	for question in PreTestQuestion.objects.all():
		questionobjectlist.append(question)	
	
	#add answers to question 2
	for j in range(0,2):
		add_answer(questionobjectlist[2], preanswerlist[j])
	
	#add answer to question 3
	for k in range(2, 6):
		add_answer(questionobjectlist[3], preanswerlist[k])

	#add answer to question 4
	for l in range(6,9):
		add_answer(questionobjectlist[4], preanswerlist[l])

	#add answer to question 5
	for m in range(9, 13):
		add_answer(questionobjectlist[5], preanswerlist[m])

	#add answer to question 6
	for n in range(13, 16):
		add_answer(questionobjectlist[6], preanswerlist[n])

	#add answer to question 7
	for p in range(16, len(preanswerlist)):
		add_answer(questionobjectlist[7], preanswerlist[p])
	
	#print answers to screen
	for a in PreTestAnswer.objects.all():
		print str(a)

def add_question(question, question_number):
	p = PreTestQuestion.objects.get_or_create(question=question, question_number=question_number)[0]
	return p
def add_answer(question, choices, votes=0):
	c = PreTestAnswer.objects.get_or_create(answer=question, choices=choices, votes=votes)[0]
	return c

if __name__ == '__main__':
	print "Inscribing questions into database..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE',"sunstreet.settings")
	from lifeskills.models import PreTestQuestion
	from lifeskills.models import PreTestAnswer
	populate()
