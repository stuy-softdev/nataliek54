#Natalie Keiger
#Team 1
#SoftDev
#skeleton/stub :: SQLITE3 BASICS
#Oct 2025

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops -- you will use cursor to trigger db events

#==========================================================

#loop through dict reader to get each student and add them to table
c.execute("DROP TABLE IF EXISTS students")
c.execute("DROP TABLE IF EXISTS courses")
         # test SQL stmt in sqlite3 shell, save as string
c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);")

with open('students-beeg.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO students VALUES ( '" + row['name'] + "', '" +
                    row['age'] + "', '" + row['id'] + "');")
        
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")

with open('courses-beeg.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        c.execute("INSERT INTO courses VALUES ( '" + row['code'] + "', '" +
                    row['mark'] + "', '" + row['id'] + "');")
        
#print everything
print("List of all students:")
studes = c.execute("SELECT name FROM students;")
print(studes.fetchall())
print("List of all students ^=========================================================")

#all courses
print("List of all courses:")
course = c.execute("SELECT code FROM courses;")
print(studes.fetchall())
print("List of all courses ^=========================================================")
#==========================================================

#students above 50
print("List of all students older than 50:")
studes = c.execute("SELECT name FROM students WHERE age>50;")
print(studes.fetchall())
print("List of all students older than 50^=========================================================")

#all grades for a specific student
print("List of all grades for student 1:")
studes = c.execute("SELECT mark FROM courses WHERE id=1;")
print(studes.fetchall())
print("List of all grades for student 1 ^=========================================================")

#all students for specific course
print("List of all students for ai:")
liststudes = c.execute("SELECT id FROM courses WHERE code='ai';")
print(liststudes.fetchall())
print("List of all students for ai ^=========================================================")
db.commit() #save changes
db.close()  #close database

