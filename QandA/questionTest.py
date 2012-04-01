import makeQuery

#*This uses the makeQuery class to ask questions.
#
#*Initially it starts in question mode, answers are 
#case sensitve right now.
#
#*enter 'stop' to enter command mode where you can
#change the country and level of difficulty.
#
#*enter 'help' in command mode to get list of all
#commands

def questionMode(x, obj):
	rightAns = obj.getRightAnswer()
	while (x != 'stop' and x != 'quit'):

		if(x == rightAns):
	 		print('You are 100% correct')
		else:
			print('Wrong!')
	
		obj.newQuestion();
		print obj.getCurrQuestion()
		x = raw_input()
		rightAns = obj.getRightAnswer()
	return x

def commandMode(x, obj):
	while ( x != 'resume' and x != 'quit'):
		print '=>',
		x = raw_input()
		command = x.split()
		print command
		if (len(command) >= 2):
			s = ' '.join(command[1:])
			print s
			if(command[0] == 'changec' and obj.isCountry(s)):
				obj.changeQuestionTopic(s)

			elif(command[0] == 'changel' and obj.isLevel(int(s))):
				obj.changeQuestionLevel(int(command[1]))
			
			elif(not obj.isCountry(s)):
				print 'No country "' + s + '" in the database'
		
			elif(not obj.isLevel(int(s))):
				print 'No level ' + s + ' for this country in the database'
			else:
				print 'invalid command or arg.'
		elif(x == 'help'):
			print 'changec [String] ==> changes country that you want questions for'
			print 'changel [int] ==> change the difficulty level for the questions'					
			print 'stop ==> when in question mode this brings you to command mode'
			print 'resume ==> resume question mode from command mode'
			print 'quit ==> exit program'
	return x
#*******************************************
obj = makeQuery.makeQuery('Mexico',1)

print obj.getCurrQuestion()
x = raw_input()

#loop to ask new question in catigory specified above.
while (x != 'quit'):
	x = questionMode(x, obj)
	x = commandMode(x, obj)
	

	
