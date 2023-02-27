import sqlite3

connection = sqlite3.connect('students.db')
cur = connection.cursor()

table = '''CREATE TABLE Students
	(Student TEXT PRIMARY KEY	NOT NULL,
	ID		INTEGER		NOT NULL,
	Score		INTEGER		NOT NULL);'''
cur.execute(table)

cur.execute("INSERT INTO students (Student, ID, Score) VALUES (?, ?, ?)", ('Steve Smith', 211, 80))
cur.execute("INSERT INTO students (Student, ID, Score) VALUES (?, ?, ?)", ('Jian Wong', 122, 92))
cur.execute("INSERT INTO students (Student, ID, Score) VALUES (?, ?, ?)", ('Chris Peterson', 213, 93))
cur.execute("INSERT INTO students (Student, ID, Score) VALUES (?, ?, ?)", ('Sai Patel', 524, 94))
cur.execute("INSERT INTO students (Student, ID, Score) VALUES (?, ?, ?)", ('Andrew Whitehead', 425, 99))
cur.execute("INSERT INTO students (Student, ID, Score) VALUES (?, ?, ?)", ('Lynn Roberts', 626, 90))
cur.execute("INSERT INTO students (Student, ID, Score) VALUES (?, ?, ?)", ('Robert Sanders', 287, 75))
cur.execute("INSERT INTO students (Student, ID, Score) VALUES (?, ?, ?)", ('George Washington', 424, 89))

connection.commit()
connection.close()
