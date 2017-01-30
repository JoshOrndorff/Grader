#! /usr/bin/python3

import sqlite3
import argparse

def init_db(cur):
  """ Adds necessary tables to a blank darabase. """
  
  # Create students table
  cur.execute("""CREATE TABLE Students(id INTEGER PRIMARY KEY,
                                       fname VARCHAR(32),
                                       lname VARCHAR(32),
                                       cname VARCHAR(32),
                                       gender CHAR(1)
                                      )""")
  # Create assignments table
  cur.execute("""CREATE TABLE Assignments(id INTEGER PRIMARY KEY,
                                          name VARCHAR(32),
                                          desc VARCHAR(255),
                                          points INTEGER
                                         )""")
  
  # Create GradeEntries table
  cur.execute("""CREATE TABLE GradeEntries(student INTEGER REFERENCES Students(id),
                                           assignment INTEGER REFERENCES Assignments(id),
                                           points INTEGER,
                                           PRIMARY KEY (student, assignment)
                                          )""")

  # Create tags table
  cur.execute("""CREATE TABLE Tags(id INTEGER PRIMARY KEY,
                                   name VARCHAR(32),
                                   desc VARCHAR(255)
                                  )""")
  
  # Create GradeEntries table
  cur.execute("""CREATE TABLE TagAttachments(tag INTEGER REFERENCES Tags(id),
                                             assignment INTEGER REFERENCES Assignments(id),
                                             PRIMARY KEY (tag, assignment)
                                            )""")



def validate_db(cur):
  """
  Given a databse, validates its integrety as a grader database.
  
  Not really checking anything currently.
  """
  #TODO confirm all the tables and schema are correct.
  
  #TODO Confirm each grade entry has a valid student and assignment
  
  #TODO Confirm each tagging has a valid tag and assignment
  
  return True



def init_command(args, cur):
  # Nothing useful comes in in args here, but it is still taken to keep the signature consistent with other command functions.
  
  # If db is empty, initialize it
  sql = "SELECT name FROM sqlite_master WHERE type='table';"
  cur.execute(sql)
  tables = cur.fetchall()
  if len(tables) == 0:
    print("Initializing tables.")
    init_db(cur)
  
  # Verify the database
  if validate_db(cur):
    print("Database passes validation checks.")
  else:
    print("Database fails validation checks.") #TODO reproduce sqlite errors here.


  
  
  
  
  
  
  
  
