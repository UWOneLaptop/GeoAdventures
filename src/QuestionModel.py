
class QuestionQuery:

    def __init__(self):
        """constructor"""
        return Non;
        

    def getQuestions(self,country):
        '''returns one question per building'''
        return None;#skeleton

    def generateQuestions(self):
        '''this method generates new questions per country'''
        return None;#skeleton

    def getAnswers(self, q_id):
        '''Gets all answers for a given question (id)'''
        return None;#skeleton

    def getSingleQuestion(self, q_id):
        '''Gets new Question of different q_id than previous q_id'''
        return None;#skeleton

    def getHint(self, q_id):
        '''returns hint for question passed'''
        return None;#skeleton
        

class Question:
    
    def __init__(self, question, answer, choices, buildingTag, q_id):
        '''constructor'''
        self.question = question
        self.answer = answer
        self.choices = choices
        self.buildlingTag = buildingTag
        self.q_id = q_id

    def getQuestion(self):
        '''returns question from database with q_id'''
        return self.question

    def getAnswer(self):
        '''returns answer of question'''
        #return dataBaseCall()
        return None;#skeleton

    def isCorrect(self, answerAttempt):
        '''returns boolean'''
        #return answerAttempt == dataBaseCall(rightAnsId)
        return None;#skeleton
    
