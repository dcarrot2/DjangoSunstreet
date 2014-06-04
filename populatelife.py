import os


def populate():
	prequestionlist = ["What is the main thing you learned from the Life Skills training class?",
			"How has the class changed the way you act?",
			"Did you talk with your family or friends about what you learned in the class?", "Has the class changed the amount of alcohol or drugs you use?", "How likely are you to be involved in violent or 'risky' behavior now?","Which best describes how much you have been involved in gang activity over the last 30 days: (check one)", "Has the class changed your attitudes about gangs?","Overall, how important is this class to you life?"]

	for i in range(0, len(prequestionlist)):
		add_question(question=prequestionlist[i], question_number= i+1)

	for q in PreTestQuestion.objects.all():
		print str(q)

def add_question(question, question_number):
	p = PreTestQuestion.objects.get_or_create(question=question, question_number=question_number)[0]
	return p


if __name__ == '__main__':
	print "Inscribing questions into database..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE',"sunstreet.settings")
	from lifeskills.models import PreTestQuestion
	populate()
