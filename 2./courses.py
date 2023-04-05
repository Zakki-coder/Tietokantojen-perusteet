import os
import sqlite3

# delete if exists
path_to_db = "courses.db"
if os.path.exists(path_to_db):
	os.remove(path_to_db)

db = sqlite3.connect(path_to_db)
db.isolation_level = None

# luo tietokantaan tarvittavat taulut
# opettajia, kursseja, opiskelijoita, suorituksia ja ryhmiä
def create_tables():
	db.execute("CREATE TABLE Teachers ( \
		id INTEGER PRIMARY KEY, \
		name TEXT \
	)")

	db.execute("CREATE TABLE Students ( \
		id INTEGER PRIMARY KEY, \
		name TEXT \
	)")

	db.execute("CREATE TABLE Courses ( \
		id INTEGER PRIMARY KEY, \
		name TEXT, \
		credits INTEGER \
	)")

	db.execute("CREATE TABLE Course_teachers ( \
		id INTEGER PRIMARY KEY, \
		course_id INTEGER, \
		teacher_id INTEGER \
	)")

	db.execute("CREATE TABLE Credits ( \
		id INTEGER PRIMARY KEY, \
		student_id INTEGER, \
		course_id INTEGER, \
		date INTEGER, \
		grade INTEGER \
	)")

	db.execute("CREATE TABLE Groups ( \
		id INTEGER PRIMARY KEY, \
		name TEXT \
	)")

	db.execute("CREATE TABLE Group_teachers ( \
		id INTEGER PRIMARY KEY, \
		group_id INTEGER, \
		teacher_id INTEGER \
	)")

	db.execute("CREATE TABLE Group_students ( \
		id INTEGER PRIMARY KEY, \
		group_id INTEGER, \
		student_id INTEGER \
	)")

# lisää opettajan tietokantaan
# Return teacher ID
def create_teacher(name):
	db.execute("INSERT INTO Teachers (name) VALUES (?)", [name])
	res = db.execute("SELECT id FROM Teachers ORDER BY id DESC LIMIT 1").fetchone()[0]
	return res

# print table
def print_table(table):
	for row in db.execute("SELECT * FROM " + table):
		print(row)
	print()

# lisää kurssin tietokantaan
# Return course ID
def create_course(name, credits, teacher_ids):
	db.execute("INSERT INTO Courses (name, credits) VALUES (?, ?)", (name, credits))
	course_id = db.execute("SELECT id FROM Courses ORDER BY id DESC LIMIT 1").fetchone()[0]
	for id in teacher_ids:
		db.execute("INSERT INTO Course_teachers (course_id, teacher_id) VALUES (?, ?)", (course_id, id))
	return course_id

# lisää opiskelijan tietokantaan
# Return student ID
def create_student(name):
	db.execute("INSERT INTO Students (name) VALUES (?)", [name])
	student_id = db.execute("SELECT id FROM Students ORDER BY id DESC LIMIT 1").fetchone()[0]
	return student_id

# antaa opiskelijalle suorituksen kurssista

def add_credits(student_id, course_id, date, grade):
	db.execute("INSERT INTO Credits (student_id, course_id, date, grade) VALUES (?, ?, ?, ?)", (student_id, course_id, date, grade))

# lisää ryhmän tietokantaan
def create_group(name, teacher_ids, student_ids):
	db.execute("INSERT INTO Groups (name) VALUES (?)", [name])
	group_id = db.execute("SELECT id FROM Groups ORDER BY id LIMIT 1").fetchone()[0]
	for id in teacher_ids:
		db.execute("INSERT INTO Group_teachers (group_id, teacher_id) VALUES (?, ?)", (group_id, id))
	for id in student_ids:
		db.execute("INSERT INTO Group_students (group_id, student_id) VALUES (?, ?)", (group_id, id))

# hakee kurssit, joissa opettaja opettaa (aakkosjärjestyksessä)
def courses_by_teacher(teacher_name):
	courses = db.execute("SELECT C.name FROM Course_teachers CT JOIN Courses C ON CT.course_id = C.id JOIN Teachers ON CT.teacher_id = Teachers.id WHERE Teachers.name = ?", [teacher_name]).fetchall()
	return courses

# hakee opettajan antamien opintopisteiden määrän
def credits_by_teacher(teacher_name):
	pass

# hakee opiskelijan suorittamat kurssit arvosanoineen (aakkosjärjestyksessä)
def courses_by_student(student_name):
	pass

# hakee tiettynä vuonna saatujen opintopisteiden määrän
def credits_by_year(year):
	pass

# hakee kurssin arvosanojen jakauman (järjestyksessä arvosanat 1-5)
def grade_distribution(course_name):
	pass

# hakee listan kursseista (nimi, opettajien määrä, suorittajien määrä) (aakkosjärjestyksessä)
def course_list():
	pass

# hakee listan opettajista kursseineen (aakkosjärjestyksessä opettajat ja kurssit)
def teacher_list():
	pass

# hakee ryhmässä olevat henkilöt (aakkosjärjestyksessä)
def group_people(group_name):
	pass

# hakee ryhmissä saatujen opintopisteiden määrät (aakkosjärjestyksessä)
def credits_in_groups():
	pass

# hakee ryhmät, joissa on tietty opettaja ja opiskelija (aakkosjärjestyksessä)
def common_groups(teacher_name, student_name):
	pass