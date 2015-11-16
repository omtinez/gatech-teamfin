import sqlite3

db = sqlite3.connect("database/jogrx.db")
fd = open('database/schema.sql', 'r')
script = fd.read()
db.executescript(script)
fd.close()
