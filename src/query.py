
class QuestionQuery:
    """
    A question query is an iterator that returns all possible questions that could be asked given a set of tags
    After the question query is initialized, the getQuestions(...) method should be called to populate the itereator
    with questions
    each individual question is called by the method getSingleQuestion(...)
    """
    def __init__(self,database_path):
        """constructor, accepts a path to the database to open"""
        self.database = database_path
    
    def generate_questions(self,tags):
		'''
		Returns a list of Question objects that match the specified set of tags.
		The tags specify the subject of the question and includes the country name
		that the question will be about.
		'''
        import sqlite3 as sqlite
        con = sqlite.connect(self.database);
        cur = con.cursor();

		q_list = list()

		# query the DB cursor, filtering on tags
        return None;#skeleton


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
		return None
		
