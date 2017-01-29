#! /usr/bin/python3

import sqlite3
import argparse

from os.path import isfile



DEFAULT_FILENAME = "dbgrades.db"

def init_db(filename = DEFAULT_FILENAME):
  """ Creates a new database file and creates the tables. """
  
  # If the file already exists, abort
  if isfile(filename):
    message = "File {} already exists. Cannot create database.".format(filename)
    raise Exception(message)
  
  
  with sqlite3.connect(filename) as connection:
    c = connection.cursor()
    
    # Create students table
    c.execute("""CREATE TABLE Students(id INTEGER PRIMARY KEY,
                                       fname VARCHAR(32),
                                       lname VARCHAR(32),
                                       cname VARCHAR(32),
                                       gender CHAR(1)
                                      )""")
    # Create assignments table
    c.execute("""CREATE TABLE Assignments(id INTEGER PRIMARY KEY,
                                          name VARCHAR(32),
                                          desc VARCHAR(255),
                                          points INTEGER
                                         )""")
    
    # Create GradeEntries table
    c.execute("""CREATE TABLE GradeEntries(student INTEGER REFERENCES Students(id),
                                           assignment INTEGER REFERENCES Assignments(id),
                                           points INTEGER,
                                           PRIMARY KEY (student, assignment)
                                          )""")

    # Create tags table
    c.execute("""CREATE TABLE Tags(id INTEGER PRIMARY KEY,
                                      name VARCHAR(32),
                                      desc VARCHAR(255)
                                  )""")
    
    # Create GradeEntries table
    c.execute("""CREATE TABLE TagAttachments(tag INTEGER REFERENCES Tags(id),
                                             assignment INTEGER REFERENCES Assignments(id),
                                             PRIMARY KEY (tag, assignment)
                                          )""")



def validate_db(filename = DEFAULT_FILENAME):
  """
  Given a databse, validates its integrety as a grader database.
  
  Not really checking much currently.
  """
  
  # Confirm each grade entry has a valid student and assignment
  
  # Confirm each tagging has a valid tag and assignment
  
  return True



if __name__ == "__main__":
  # Parse the arguments to figure out what we want to do.
  parser = argparse.ArgumentParser("A simple commandline gradebook utility that stays out of your way.")
  parser.add_argument("init", help="Initialize a new database.")
  
  init_db()
  
  
  
  
  
  
  
  
  
  
  
