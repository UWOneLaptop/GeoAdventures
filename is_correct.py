def substCost(x, y):
	if x == y:
		return 0
	else:
		return 1

def minedit(target, source):
	"""Calculate minimum edit distance of inputted entry and real answer."""

	# target
	i = len(target)
	# source
	j = len(source)
	
	if i == 0:
		return j
	elif j == 0:
		return i
	
	return(min(minedit(target[:i-1], source) + 1, minedit(target, source[:j-1])+1, minedit(target[:i-1], source[:j-1])+substCost(source[j-1], target[i-1])))

def spellfudge(entry, answer):
	entry = entry.lower()
	correct = answer.lower()

	if entry == answer:
		return 0

	return minedit(entry, answer)

def is_correct(entry, answer):
	minedit_value = spellfudge(entry, answer)
	if minedit_value == 0:
		return "You are correct!"
	if minedit_value == 1 or (minedit_value == 2 and len(answer) > 5):
		return "You're very very close! Correct answer was %s, but we'll give it to you anyways." % answer
	else:
		return "Wrong! Correct answer was %s." % answer

def checkAnswer(question, answer):
	return spellFudge(answer, question.answer)
