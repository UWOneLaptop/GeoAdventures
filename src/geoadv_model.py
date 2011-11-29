import sqlite3

class GeoAdvModel:
	'''This is where the state of the game exists as well as
	any interaction with the database.'''

	#current states of the program
	old_questions = {}	#old questions
	connection #	connection to DB
	r	#random number
	cur_question #curent question


	def __init__(self, database):
		'''initializes the model with the specified database'''
		connection = sqlite3.connect(database)
		r = random.seed(gmtime() * 69) # random on current time multiplied by best number 

		
	#pseudo
	def nextQuestion(self, country):
		countries = connection.cursor()
		question = connection.cursor()	
		symbol1 = (country,)
		table.execute('select * from questions where cid = (select cid from countries where name = ?)',symbol1); 
		possible_question = {}
		for row in table:
			if row[0] not in old_questions:
				possiblequestion.append(row)
		b = r.randint(0,possible_question.length())
		return_row = possible_question[b]	
		old_question.append(return_row[0])
		cur_question = return_row