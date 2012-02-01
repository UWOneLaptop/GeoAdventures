import sqlite3

conn = sqlite3.connect('countries.db')

c = conn.cursor()

c.execute("""insert into countries values(2, "France")""")

conn.commit()

c.close()
