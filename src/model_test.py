from model import *

m = Model(dict())
q = m.c_query.generate_countries("Mexico", 2)
q = m.q_query.generate_questions( ("Mexico",) )
print ("RESULTS")
print (str(q))
#print str(m.q_query.generate_questions( ["mexico"] ))
