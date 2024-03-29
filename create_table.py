import sqlite3

conn = sqlite3.connect('students.sqlite')
print("connected to database successfully")

conn.execute('CREATE TABLE students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, addr TEXT, city TEXT, zip TEXT)')
print("table created successfully")

conn.close()