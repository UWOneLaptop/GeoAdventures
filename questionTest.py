import makeQuery

obj = makeQuery.makeQuery('Mexico',1)

print obj.getQuestion()
x = raw_input();
rightAns = obj.getRightAnswer()

#loop to ask new question in catigory specified above.
while (x != "q"):

	if(x == rightAns):
 		print('You are 100% correct')
	else:
		print('Wrong!')
	
	obj.newQuestion();
	print obj.getQuestion()
	x = raw_input()
	rightAns = obj.getRightAnswer()

