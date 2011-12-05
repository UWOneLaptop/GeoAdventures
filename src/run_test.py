import sqlite3
import geoadv_controller
import geoadv_model

def print_cursor(cursor):
	for row in m.cursor:
		for ele in row:
			print ele





# main
print "ye scurvy dog, welcome to your doom!"
database_name = raw_input("database ya be wantin? ")

print "building th' game..."
m = GeoAdvModel(database_name)
c = GeoAdvController(m)

country = raw_input("yer country?")
m.nextQuestion(country);
print m.cur_question