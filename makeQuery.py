import sqlite3
import random

#If you want to add stuff to db enter .schema for the
#schema to get attribute names in sqlite3.

class makeQuery:
	#stuff for connecting sqlite3
	con = sqlite3.connect('QandA.db')
	c = con.cursor()
	
	#initialize with country name and difficulty level.
	def __init__(self, c, dl):
		self.country = c
		self.diffLevel = dl
		self.questionList = self.getQList()
		self.currQuestion = self.getQuestion()
		self.answerList = self.getAList()
	
	#Query the db
	#returns allRows from the query.
	#for internal use
	def getQList(self):
		t = (self.diffLevel, self.country, )
		#gets all rows with same country and difficulty
		self.c.execute('SELECT id, question  FROM' + \
		' questions WHERE level=? And name=?', t)
		allRows = self.c.fetchall()
		return allRows
	
	
	#Query the db
	#returns the list of possible answers to the current question
	#for internal use.
	def getAList(self):
		qInfo = self.currQuestion
		qid = qInfo[0]
		t = (qid, )
		self.c.execute('SELECT valid_ans, answer FROM'+ \
		 ' answers WHERE qid=?', t)
		allRows = self.c.fetchall()
		return allRows
	
	#retruns the current question as a String
	def getQuestion(self):
		index = random.random() * len(self.questionList)
		return self.questionList[int(index)]
	
	#generates new question in current difflevel and country
	#catagory.
	def newQuestion(self):
		self.currQuestion = self.getQuestion()
		self.answerList = self.getAList() 	
	
	#finds the right answer from the list of answers.
	def getRightAnswer(self):
		rightAns = ""
		for x in self.answerList:
			if x[0] == 1:
				rightAns = x[1]
		return rightAns
	
	#change the question topic, default level is 1.
	def changeQuestionTopic(self, c):
		self.country = c
		self.changeQuestionLevel(1)

	#change the question difficulty level.
	def changeQuestionLevel(self, dl):
		self.diffLevel = dl
		self.questionList = self.getQList()
		self.currQuestion = self.getQuestion()
		self.answerList = self.getAList()

	#tests if a country is present in the db. returns true if
	#there is and false if there is not.
	def isCountry(self, c):
		t = (self.diffLevel, c, )
		self.c.execute('SELECT DISTINCT name  FROM' + \
		' questions WHERE level=? And name=?', t)
		allRows = self.c.fetchall()
	
		if (len(allRows) == 0):
			return 0
		else:
			return 1
	
	def isLevel(self, dl):
		t = (dl, self.country, )
		self.c.execute('SELECT DISTINCT name  FROM' + \
		' questions WHERE level=? And name=?', t)
		allRows = self.c.fetchall()
	
		if (len(allRows) == 0):
			return 0
		else:
			return 1

	#returns current question
	def getCurrQuestion(self):
		return self.currQuestion[1]

	#returns just the list of answers
	def getAnswerList(self):
		return self.answerList
	
	#returns the current country
	def getCountry(self):
		return self.country

	#returns the current difficulty level
	def getLevel(self):
		return self.diffLevel

