from Question import *
from is_correct import *
from array import *
import pygtk
import gtk


def main():
    wrong_count = 0
    n_until_hint = 5
    correct = False
# get a question
    question = Question(1, "what is the starting fire pokemon", "charmander", "you need a hint??", "Charmander")
    question2 = Question(2, "what is the starting fire pokemon", "aa", "you need a hint??", "Charmander")
    question_list = [question, question2]
    for i in range(len(question_list)):
        while(not correct):
            correct = ask_question(question_list[i])
            if not correct:
                wrong_count = wrong_count + 1
                if(wrong_count >= n_until_hint):
                    print str(get_hint(question_list[i]))
        
        if i + 1 < len(question_list):
            correct = False

        print("You were right!")



"""returns true if exact match"""
def ask_question(question):
    answer = raw_input(question.text + " - ")
    return checkAnswer(question, answer) == 0


def get_hint(question):
#possible multiple hints?
    return question.hints


	
if __name__ == '__main__': main()
