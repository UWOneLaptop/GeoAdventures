from model import *

m = Model(dict())
q = m.c_query.generate_countries("mexico", 2)
print "RESULTS"
print str(q)
#print str(m.q_query.generate_questions( ["mexico"] ))
