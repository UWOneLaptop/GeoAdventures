if __name__ == '__main__': main()

def main():
	wrong_count = 0
	n_until_hint = 0
	correct = False
	while(not correct):
		correct = ask_question(question)
		if(wrong_count >= n_until_hint):
			getHint(question)
	print("You were right!")
		


"""returns true if exact match"""
def ask_question(question):
	answer = input(question.text)
	return checkAnswer(question, answer) == 0
	

def get_hint(question):
	#possible multiple hints?
	return question.hints


	
