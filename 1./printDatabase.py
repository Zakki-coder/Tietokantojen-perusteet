"""
Load all tables from the database and print them to the console.
"""

import sqlite3

# Connect to the database
db = sqlite3.connect('bikes.db')
db.isolation_level = None

# Get a cursor to the database
cursor = db.cursor()

# Get all tables from the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Print all tables
for table in tables:
	print(table[0])
	cursor.execute("SELECT * FROM " + table[0])
	# Print the column names
	print([description[0] for description in cursor.description])
	# Print 10 rows
	for i in range(10):
		print(cursor.fetchone())
	# rows = cursor.fetchall()
	# for row in rows:
	# 	print(row)
	print() # Print a blank line