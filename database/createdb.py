import sqlite3

db = sqlite3.connect("database/jogrx.db")
db.execute("CREATE TABLE hisp (id INTEGER PRIMARY KEY, server text NOT NULL)")
