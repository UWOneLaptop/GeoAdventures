import sqlite3
import random

class makeQuery:
	#stuff for connecting sqlite3
	con = sqlite3.connect('QandA')
	c = con.cursor()
	
	#initialize with country name and difficulty level.
	def __init__(self, c, dl):
		self.country = c
		self.diffLevel = dl
		self.QandA = self.getQandA()
	
	#Query the db
	#returns random row from allRows and returns the tuple.
	#for internal use
	def getQ(self):
		t = (self.diffLevel, self.country, )
		#gets all rows with same country and difficulty
		self.c.execute('SELECT id, question  FROM' + \
		' questions WHERE level=? And name=?', t)
		allRows = self.c.fetchall()
		index = int(random.random()*len(allRows))
		return allRows[index]
	
	
	#Query the db
	#returns tuple containing the question and answer(s)
	#for internal use.
	def getA(self):
		qInfo = self.getQ()
		qid = qInfo[0]
		q = qInfo[1]
		t = (qid, )
		self.c.execute('SELECT valid_ans, answer FROM'+ \
		 ' answers WHERE qid=?', t)
		allRows = self.c.fetchall()
		return (q, allRows)

	#returns the question and all possible answers as a tuple
	#for internal use. 
	def getQandA(self):
		return self.getA()
	
	#retruns the current question as a String
	def getQuestion(self):
		return self.QandA[0]
	
	#generates new question in current difflevel and country
	#catagory.
	def newQuestion(self):
		self.QandA = self.getQandA()
	
	#returns just the list of answers
	def getAnswerList(self):
		return self.QandA[1] 
	
	#finds the right answer from the list of answers.
	def getRightAnswer(self):
		rightAns = ""
		for x in self.QandA[1]:
			if x[0] == 1:
				rightAns = x[1]
		return rightAns
	
	#change the difficulty level.
	def setDiffLevel(self, dl):
		self.diffLevel = dl
	
	#change the country.
	def setCountry(self, c):
		self.country = c
