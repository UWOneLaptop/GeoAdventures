
class Model:
	''' The Model is what the View talks to to get the current state of the game
	and change that state.  It should expose functions that both give out game
	state info as well as changes game state.  Its fields should keep track of
	the game state '''

	def __init__():
		'''setup connections to the database and init game state variables'''
		return None  # skeleton code

	def setup_game(player_info_hash):
		'''accepts a hash of player info
			'name' -> player name
			'gender' -> player gender
			'country' -> starting country for the game
		'''
		return None  # skeleton code

	def new_game(start_country):
		'''generates a new game with 15 new countries including the start
		country.'''
		# list of info tuples for a country (i.e. name, tags, etc)
		country_list = get_countries(start_country)
		for x in country_list:
			name,tags = x
			facts, questions = question_query(x)
			building_query(tags)
			CountryInstance(name,tags,facts,questions)
		return None  # skeleton code


	def enter_country(country_id):
		'''enter the specified country, generating buildings and questions if
		never visited before.'''
		return None  # skeleton code




class CountryInstance:
	''' Contains state info for a country relating to the current game.
	Keeps track of buildings, questions at building, fact sheets, etc.'''
	
	def __init__(self,name,tags,facts,questions):
		self.buildings
		self.facts = facts
		self.name = name
		for i in range (len(tags)) :
			builings[i] = (tags[i], questions[i])
		
		return None

	def fact_sheet(fact_array):
		return None # skeleton code
		
	'''def makeBuildings(tag, question):
		new BuildingInstance(tag, Question)'''

'''class BuildingInstance:
	'''Contains info for a building.  This will be intiallized when the buildings database and questions databases get queried.  An array of buildings will be held in a CountryInstance.
	The type is the style of building i.e. cathedral, library etc.  Type is also expected to hold the character in the builidng.  The Question holds the question-answer pair.'''
	
	def __init__(self, type, Question):
'''		return None
