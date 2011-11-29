from event_hook import *

class GeoAdvController:
	'''this picks up event firings from the view and executes the
	appropriate victi-- i mean functions in the model'''

	def __init__(self, model):
		self.model = model

		# called when the user answers a question with answer as parameter
		self.answer_ques_handler = EventHook()
		self.setup_answer_ques_h()

		# called when the current question should be displayed to the user
		self.display_ques_handler = EventHook()
		self.setup_display_ques_h()


'''An example of how to use an event hook:
> 
> def party:
> 	print "have fun, rock out, throw turtles"
> 
> ev = EventHook()
> ev += party
> 
> ev.fire()
have fun, rock out, throw turtles

'''
