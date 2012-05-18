from queries import *

class QuestionQuery:
	"""
	A question query is an iterator that returns all possible questions that could be asked given a set of tags
	After the question query is initialized, the getQuestions(...) method should be called to populate the itereator
	with questions
	each individual question is called by the method getSingleQuestion(...)
	"""
	def __init__(self,database_path):
		"""constructor, accepts a path to the database to open"""
		self.database_path = database_path
	
	def generate_questions(self,tags):
		'''
		Returns a list of Question objects that match the specified set of tags.
		The tags specify the subject of the question and includes the country name
		that the question will be about.
		'''
		from question import Question
		import sqlite3 as sqlite
		db = sqlite.connect(self.database_path);
		cur = db.cursor();

		q_list = list()

		if len(tags) == 1:
			cur.execute(get_question_by_tag(tags[0]))
		else:
			cur.execute(get_question_by_tags(tags))

		print "Query Questions"
		for row in cur.fetchall():
			print str(row)
			#???? = row.split(",")
			#extract values
			text = None
			answer = None
			choices = None
			q_id = None

			q_list.append(Question(text, answer, choices, q_id))

		db.close()
		return q_list


class CountryQuery:

	def __init__(self,database_path):
		"""constructor, accepts a path to the database to open"""
		self.database_path = database_path


	def generate_countries(self, start_country, number):
		'''
		Returns a list of countries of the specifid number which
		includes the specified starting country.
		The list is a list of hashes that map information about the
		country as specific attributes.  For example:
			list[0]["name"] = the name of the first country in the list.
			list[4]["tags"] = a tuple of tags for the 5th country in the list.

		The current set of expected attributes are:
			"name" - the name of the country
			"tags" - a tuple of tags for this country (including the country name)
		''' 
		import sqlite3 as sqlite
		db = sqlite.connect(self.database_path)
		c = db.cursor()

		id_list = list()
		chosen_list = list()

		print "Query Countries"
		c.execute( query_countries() )
		for row in c.fetchall():
			print str(row)
			c_id, name = row
			pair = (c_id, str(name),)

			# Make sure we add the intended start country
			if name == start_country:
				chosen_list.append(pair)
			id_list.append(pair)

		from random import choice
		if len(id_list) > number:
			# Choose the rest of the countries randomly
			while len(chosen_list) < number:
				chosen_list.append( choice(id_list) )
		else:
			chosen_list = id_list


		print "Query Country Info"
		info_hash_list = list()
		for c_id, name in chosen_list:
			c.execute( get_tags(c_id) )
			info_dict = dict()
			#extract the info for this country
			for row in c.fetchall():
				tags = list()
				for r in list(row):
					tags.append(str(r))
				tags = tuple(tags)
			# put info into the dict
			info_dict["name"] = name
			info_dict["tags"] = tags 

			info_hash_list.append(info_dict)
				
		db.close()
		return info_hash_list

