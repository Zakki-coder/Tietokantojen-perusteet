import sqlite3
import math

# Connect to the database
db = sqlite3.connect('bikes.db')
db.isolation_level = None

# Get a cursor to the database

# Print table
def print_table(table):
	for row in table:
		print(row)

# Define function to get the distance of a user
def distance_of_user(user):
	# Get user id
	row = db.execute("SELECT id FROM Users WHERE name=?", [user]) #.fetchone()
	user_id = row.fetchone()
	# Get sum of distances
	sum_of_distances = db.execute("SELECT SUM(distance) FROM Trips WHERE user_id=?", [user_id[0]]).fetchall()
	#print(f"Sum of distances: {sum_of_distances[0][0]}")
	return(sum_of_distances[0][0])

# Function that returns the average speed of user
def speed_of_user(user):
	# Calculate distance / time
	user_id = db.execute("SELECT id FROM Users WHERE name=?", [user]).fetchone()
	trip_times = db.execute("SELECT SUM(duration) FROM Trips WHERE user_id=?", [user_id[0]]).fetchone()
	# Convert minutes to hours
	trip_times_in_hours = trip_times[0] / 60
	# Divide with 1000 to convert meters into kilometers
	return(round(distance_of_user(user) / trip_times_in_hours / 1000, 2))

# Function that tells for every city the total drive time
def duration_in_each_city(day):
	result = []
	cities = db.execute("SELECT * FROM Cities").fetchall()
	for city in cities:
		result.append((city[1], db.execute("SELECT SUM(duration) FROM Bikes JOIN Trips ON Bikes.id = Trips.bike_id WHERE city_id=? AND day=?", (city[0], day)).fetchone()[0]))
	return result

# Function that tells number of users in given city
def users_in_city(city):
	city_id = db.execute("SELECT id FROM Cities WHERE Cities.name=?", [city]).fetchone()
	number_of_users = db.execute("SELECT COUNT(DISTINCT user_id) FROM Bikes JOIN Trips ON Bikes.id = Trips.bike_id WHERE Bikes.city_id =?", [city_id[0]]).fetchone()
	return number_of_users[0]

# Function to tell the number of trips for each day on a given city
def trips_on_each_day(city):
	city_id = db.execute("SELECT id FROM Cities WHERE name=?", [city]).fetchone()
	trips = db.execute("SELECT T.day, (SELECT COUNT(*) FROM Trips JOIN Bikes ON Bikes.id = Trips.bike_id WHERE day = T.day AND Bikes.city_id=?) FROM Trips T JOIN Bikes ON Bikes.id = T.bike_id WHERE Bikes.city_id=? GROUP BY T.day ORDER BY T.day", (city_id[0], city_id[0])).fetchall()
	return trips

# Function to tell the favorite departure station of given city and the number of trips
def most_popular_start(city):
	city_id = db.execute("SELECT id FROM Cities WHERE name=?", [city]).fetchone()
	favorite = db.execute("SELECT (SELECT name FROM Stops WHERE id = start), MAX(trips) FROM (SELECT T.from_id start, COUNT(*) trips FROM Bikes JOIN Trips T ON Bikes.id = T.bike_id WHERE Bikes.city_id=? GROUP BY T.from_id)", [city_id[0]]).fetchone()
	return favorite