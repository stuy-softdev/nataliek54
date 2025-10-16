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

         # test SQL stmt in sqlite3 shell, save as string
c.execute("CREATE TABLE students (name TEXT, age INTEGER, id INTEGER);")

with open('students.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        c.execute("INSERT INTO students VALUES ( '" + row['name'] + "', '" +
                    row['age'] + "', '" + row['id'] + "');")
        
c.execute("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER);")

with open('courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)
        c.execute("INSERT INTO courses VALUES ( '" + row['code'] + "', '" +
                    row['mark'] + "', '" + row['id'] + "');")
        
    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database
