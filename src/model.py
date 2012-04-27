from query import *
from question import *

class Model:
	''' The Model is what the View talks to to get the current state of the game
	and change that state.  It should expose functions that both give out game
	state info as well as changes game state.  Its fields should keep track of
	the game state '''

	COUNTRY_LIMIT = 15

	def __init__(self, player_info_hash):
		'''
		Setup connections to the database and init game state variables
		Will automatically determine the language from the system info and
		connect the the proper database.

		Accepts a hash of player info
			"name" - player name
			"gender" - player gender
			"country" - starting country for the game
		'''
		database_path = "something"
		self.c_query = CountryQuery(database_path)
		self.q_query = QuestionQuery(database_path)
		self.player_info_hash = player_info_hash


	def new_game(self):
		'''
		Returns a new GameState object that represents a new game.
		A new game has 15 countries including the start	country of the
		current player.
		'''
		start_country = player_info_hash["country"]
		country_list = list()
		# list of info tuples for a country (i.e. name, tags, etc)
		c_info_list = c_query.generate_countries(start_country, COUNTRY_LIMIT)
		for info_hash in c_info_list:
			name = info_hash["name"]
			tags = info_hash["tags"]

			
			questions = q_query.generate_questions(tags)

			# make some buildings

			country_list.append( CountryInstance(name,tags,facts,questions) )

		return GameState(country_list, start_country)




class GameState:
	'''
	Stores the current state of the game.
	The current state includes the countries and questions available to
	the player during this game.  It also keeps track of which questions
	have been successfully answered so far and the current progress of the
	player.
	'''

	def __init__(self, country_list, start_country):
		'''		
		Accepts a list of CountryInstance objects.
		'''
		self.score = 0
		self.country_list = country_list
		self.curr_country = start_country

		enter_country(start_country)


	def enter_country(self, country_name):
		'''
		Enter the specified country in this game.
		'''
		choice = filter(lambda c: c.name == country_name, country_list)
		if len(choice) == 0:
			Exception("specified country "+country_name+" not a valid choice")
		choice = choice[0]
		self.curr_country = choice


class CountryInstance:
	''' Contains state info for a country relating to the current game.
	Keeps track of buildings, questions at building, fact sheets, etc.'''
	
	def __init__(self, name, tags, facts, questions):
		self.facts = facts
		self.name = name
		self.buildings = list()
		for i in range (len(tags)) :
			builings[i] = (tags[i], questions[i])
		
		return None

