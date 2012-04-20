from is_correct import *

class Question:
    
    def __init__(self, text, answer, choices, q_id):
        '''constructor'''
        self.text = text
        self.answer = answer
        self.choices = choices
        self.q_id = q_id

    def isCorrect(self, attempt):
        '''returns true if the attempt matches the answer or 
		is otherwise close enough.'''
		return is_correct(attempt, self.answer)
    
