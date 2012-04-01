class post_question:
    def __init__(self, database_name):
        self.myModel = GeoAdvModel(database_name)
        self.running = True
        self.myCountry = raw_input("Which country are you in now?")
    def postQuestion(self):
        while (running):
            running = raw_input("Would you like one more question?")
            if (not running):
                break
            myModel.nextQuestion()
            myQuestion = myModel.cur_qurstion
            myAnswer = raw_input(myQuestion)
            
            


# main
database_name = raw_input("database name?")

questions = post_question(database_name)
questions.postQuestion()
