from query import *
from question import *

class Model:
	''' The Model is what the View talks to to get the current state of the game
	and change that state.  It should expose functions that both give out game
	state info as well as changes game state.  Its fields should keep track of
	the game state '''

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
		self.COUNTRY_LIMIT = 15
		self.LOCATIONS_PER_COUNTRY = 3
		self.BUILDING_TYPES = ["library","townhall","museum"]
		database_path = "../database/QandA.db"
		self.c_query = CountryQuery(database_path)
		self.q_query = QuestionQuery(database_path)
		self.player_info_hash = player_info_hash


	def new_game(self):
		'''
		Returns a new GameState object that represents a new game.
		A new game has 15 countries including the start	country of the
		current player.
		'''
		start_country = self.player_info_hash["country"]

		used_q_ids = set()
		country_list = list()
		# list of info hashes, a hash for each country
		c_info_list = self.c_query.generate_countries(start_country, self.COUNTRY_LIMIT)
		for info_hash in c_info_list:
			name = info_hash["name"]
			tags = info_hash["tags"]

			# make some buildings
			buildings = self.BUILDING_TYPES[0:self.LOCATIONS_PER_COUNTRY]
			
			questions = q_query.generate_questions(tags)
			choices = filter(lambda q: q.q_id not in used_q_ids, questions)
			if len(choices) < self.LOCATIONS_PER_COUNTRY:
				Exception("specified tags "+str(tags)+" don't have enough associated questions")
				
			choices = choices[0:self.LOCATIONS_PER_COUNTRY]

			country = CountryInstance(name,facts)
			country.set_build_a(buildings[0], choices[0])
			country.set_build_b(buildings[1], choices[1])
			country.set_build_c(buildings[2], choices[2])
			country_list.append( country )

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
		self.pieces = 0
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
		elif len(choice) > 1:
			Exception("specified country "+country_name+" found multiple times")
		self.curr_country = choice[0]


	def get_country_names(self):
		'''
		Returns a list of country name visitable in this game
		'''
		return map(lambda c: c.name, self.country_list)


class CountryInstance:
	''' Contains state info for a country relating to the current game.
	Keeps track of buildings, questions at building, fact sheets, etc.'''
	
	def __init__(self, name, facts):
		self.name = name
		self.facts = facts
		self.build_a = None
		self.quest_a = None
		self.build_b = None
		self.quest_b = None
		self.build_c = None
		self.quest_c = None


	def set_build_a(b_type, question):
		self.build_a = b_type
		self.quest_a = question
		return self

	def set_build_b(b_type, question):
		self.build_b = b_type
		self.quest_b = question
		return self

	def set_build_c(b_type, question):
		self.build_c = b_type
		self.quest_c = question
		return self

