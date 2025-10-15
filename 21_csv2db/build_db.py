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

command = ""          # test SQL stmt in sqlite3 shell, save as string
command += ("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);")
c.execute(command)
command = ""

with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        command += ("INSERT INTO students VALUES ( '" + row['name'] + "', '" +
                    row['age'] + "', '" + row['id'] + "');")
        c.execute(command)
        command = ""
        
command += ("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")
c.execute(command)
command = ""

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        command += ("INSERT INTO courses VALUES ( '" + row['code'] + "', '" +
                    row['mark'] + "', '" + row['id'] + "');")
        c.execute(command)
        command = ""
        
    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
