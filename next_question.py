class next_question:
	old_questions = {}	#old questions
	connection	#	connection to DB
	r	#random number

	def __init__(self):
		connection = sqlite3.connect('~/geography')
		r = random.seed(gmtime() * 69) # random on current time multiplied by best number 
	
	#pseudo
	def nextQuestion(self, country):
		table = connection.cursor()
		symbol = (country,)
		table.execute('select * from TABLE where COUNTRY = ?', symbol)
		possible_question = {}
		for row in table:
			if row[0] not in old_questions:
				possiblequestion.append(row)
		b = r.randint(0,possible_question.length())
		return_row = possible_question[b]	
		old_question.append(return_row[0])
		return return_row