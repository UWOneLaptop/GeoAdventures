
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
		return None  # skeleton code


	def enter_country(country_id):
		'''enter the specified country, generating buildings and questions if
		never visited before.'''
		return None  # skeleton code




class CountryInstance:
	''' Contains state info for a country relating to the current game.
	Keeps track of buildings, questions at buildingo, fact sheets, etc.'''
