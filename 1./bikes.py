import sqlite3

# Connect to the database
db = sqlite3.connect('bikes.db')
db.isolation_level = None

# Get a cursor to the database

# Define function to get the distance of a user
def distance_of_user(user):
	# Get user id
	row = db.execute("SELECT id FROM Users WHERE name=?", [user]) #.fetchone()
	userName = row.fetchone()
	print(userName[0])