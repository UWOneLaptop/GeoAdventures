
class QuestionQuery:
    """
    A question query is an iterator that returns all possible questions that could be asked given a set of tags
    After the question query is initialized, the getQuestions(...) method should be called to populate the itereator
    with questions
    each individual question is called by the method getSingleQuestion(...)
    """
    def __init__(self,database_path):
        """constructor, accepts a path to the database to open"""
        self.database = database_path
        return None;
    
    def getQuestions(self,tags):
        ''' method that queries the database, populating the question list with questions from the database
            based on the tags.
        '''
        import sqlite3 as sqlite
        con = sqlite.connect(self.database);
        cur = con.cursor();

        tag_list = tags.split();
        #TODO finish working here 
        return None;#skeleton

    def generateQuestions(self,tags):
        '''method generates new questions per country'''
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
        self.q_id = q_id
        
    def getQuestion(self):
        '''returns question from database with q_id'''
        return self.question

    def getAnswer(self):
        '''returns answer of question'''
        return None;#skeleton

    def isCorrect(self, answerAttempt):
        '''returns boolean'''
        return None;#skeleton
    
