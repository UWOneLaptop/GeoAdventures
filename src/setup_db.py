import os
import sqlite3
from master_model import *
from entry_types import *

reset_db = raw_input('reset db? (y/n)')
if reset_db is 'y':
	DATABASE = raw_input("database ya be wantin? ")
	os.remove(DATABASE)
	create_database(DATABASE)


