class next_question:
	old_questions = {}	#old questions
	connection	#	connection to DB
	r	#random number
	cur_question

	def __init__(self):
		connection = sqlite3.connect('~/geography')
		r = random.seed(gmtime() * 69) # random on current time multiplied by best number 
	
	#pseudo
	def nextQuestion(self, country, profession):
		countries = connection.cursor()
		question = connection.cursor()	


		symbol1 = (country,)
		#symbol2 = (profession,)
		#table.execute('select * from questions where cid = (select cid from countries where name = ?) AND qid in (select qid from questions_tags where tid in (select tid from proftags where pid = (select pid from profession where name = ?)))',symbol1,symbol2)
		
		table.execute('select * from questions where cid = (select cid from countries where name = ?)',symbol1); 
		
		#need to fix
		possible_question = {}
		for row in table:
			if row[0] not in old_questions:
				possiblequestion.append(row)
		b = r.randint(0,possible_question.length())
		return_row = possible_question[b]	
		old_question.append(return_row[0])
		cur_question = return_row