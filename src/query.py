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

		for row in cur.fetchall():
			#???? = row.split(",")
			#extract values
			text = None
			answer = None
			choices = None
			q_id = None

			q_list.append(Question(text, answer, choices, q_id))

		self.db = sqlite.close()
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
		self.db = sqlite.connect(self.database_path)
		c = self.db.cursor()

		id_set = set()
		chosen_set = set()

		c.execute( query_countries() )
		for row in c.fetchall():
			c_id, name = row.split(",")
			if name == start_country:
				chosen_set.add(c_id)
			id_set.add(c_id)

		from random import choice
		if len(id_set) > number:
			while len(chosen_set) < number:
				chosen_set.add( random.choice(id_set) )
		else:
			chosen_set = id_set


		info_hash_list = list()
		for c_id in chosen_set:
			c.execute( get_tags(c_id) )
			info_dict = dict()
			for row in c.fetchall():
				#??? = row.split(",")
				#extract the info for this country
				name = None
				tags = None
			# put info into the dict
			info_dict["name"] = name
			info_dict["tags"] = tags 

			info_hash_list.append(info_dict)
				
		self.db = sqlite.close()
		return info_hash_list

