#! /usr/bin/python3

import argparse
import sqlite3

DEFAULT_FILENAME = "dbgrades.db"

def add_student(filename=DEFAULT_FILENAME):
  """ Interactively adds zero or one students to the database.
      All names will be automatically truncated to 32 characters.
      
      Returns whether a student was actually added.
  """
  
  print("Enter student info. (Leave first name blank to end.)")
  
  fname = input("First Name:   ")[:32]
  # Leave first name blank to enter
  if fname == "":
    return False
    
  lname  = input("Last Name:    ")[:32]
  cname  = input("Nickname:     ")[:32]
  
  gender = input("Gender (m/f): ").lower()
  if gender not in ['m', 'f']:
    print("Gender is invalid you must enter 'm' or 'f'. Student not added.")
    return False
  
  sql = """INSERT INTO 
           Students (fname, lname, cname, gender)
           VALUES ('{}', '{}', '{}', '{}')""".format(fname, lname, cname, gender)
  with sqlite3.connect(filename) as connection:
    c = connection.cursor()
    c.execute(sql)
  
  return True



def add_assignment(filename=DEFAULT_FILENAME):
  """ Interactively adds zero or one assignments to the database.
      Name will be automatically truncated to 32 characters.
      Description will be automatically truncated to 255 characters.
      
      Returns whether an assignment was actually added.
  """
  
  print("Enter Assignment info. (Leave name blank to end.)")
  
  name = input("Name:         ")[:32]
  # Leave name blank to enter
  if name == "":
    return False
    
  desc  = input("Description: ")[:255]
  points = int(input("Point Value: "))
  if points < 0:
    print("Points cannot be negative. Assignment not added.")
    return False
  
  sql = """INSERT INTO
           Assignments (name, desc, points)
           VALUES ('{}', '{}', '{}')""".format(name, desc, points)
  with sqlite3.connect(filename) as connection:
    c = connection.cursor()
    c.execute(sql)
  
  return True

  

######## Main Program ##########
parser = argparse.ArgumentParser(description='Add a student, assignment, or tag (tags not yet implemented)')
parser.add_argument('-s', '--student',    action='store_true', help="Add zero or more students to the gradebook.")
parser.add_argument('-a', '--assignment', action='store_true', help="Add zero or more assignments to the gradebook.")

args=parser.parse_args()

while args.student:
  args.student = add_student()
  
while args.assignment:
  args.assignment = add_assignment()













