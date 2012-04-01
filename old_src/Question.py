class Question:
    def __init__(self, idNum, text, answer, hints, rewards):
        self.idNum = idNum
        self.text = text
        self.answer = answer
        self.hints = hints
        self.rewards = rewards

    def console_print(self):
        answer = raw_input(self.text)

        if answer == self.answer:
            print 'Well done! It was ' + self.answer
        else:
            print 'Wrong... The right answer is ' + self.answer
