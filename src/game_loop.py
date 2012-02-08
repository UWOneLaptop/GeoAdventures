from Question import *
from is_correct import *
import pygtk
import gtk

def main():
	wrong_count = 0
	n_until_hint = 5
	correct = False
	# get a question
	question = Question(1, "what is the starting fire pokemon", "charmander", "you need a hint??", "Charmander")
	while(not correct):
		correct = ask_question(question)
		if not correct:
			wrong_count = wrong_count + 1
			if(wrong_count >= n_until_hint):
				print str(get_hint(question))
			
	print("You were right!")
		


"""returns true if exact match"""
def ask_question(question):
	answer = raw_input(question.text + " - ")
	return checkAnswer(question, answer) == 0
	

def get_hint(question):
	#possible multiple hints?
	return question.hints


	
if __name__ == '__main__': main()
