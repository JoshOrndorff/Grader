#! /usr/bin/python3

import argparse
import sqlite3
import sys

#TODO The official python tutorial explained a function to help sanitize.

def set_grade(student, assignment, points, cur):
  """
  Sets the grade for one student on one assignment.
  
  arguments are both represented as sql row tuples.
  """
  
  sql = "INSERT INTO GradeEntries VALUES({}, {}, {})".format(student[0], assignment[0], points)
  cur.execute(sql)



def update_or_set_grade(student, assignment, cur):
  """
  Sets or updates an existing grade for one student on one assignment.
  
  Arguments are both represented as sql row tuples.
  """
  #TODO
  pass



def fetch_students(partial, cur):
  """ 
  Returns all students matching the partial name pattern supplied.
  
  Returns all students if the special patter 'all' is supplied.
  """
  
  sql = "SELECT * FROM Students"
  
  if partial != '':
    sql += " WHERE fname LIKE '{0}%' OR lname LIKE '{0}%' OR cname LIKE '{0}%'".format(partial)
  
  cur.execute(sql)
    
  return cur.fetchall()



def fetch_assignments(partial, cur):
  """ 
  Returns all assignments matching the partial name pattern supplied.
  """
  
  sql = "SELECT * FROM Assignments WHERE name LIKE '{}%'".format(partial)
  
  cur.execute(sql)
    
  return cur.fetchall()




def set_command(args, cur):

  # Get all students specified
  students = fetch_students(args.student, cur)
  numStudents = len(students)

  # Now make sure partial was unique or all
  if numStudents == 0:
    print("No students matching '{}'. Use grader-query students to see roster.".format(args.student))
    sys.exit(1)

  elif numStudents > 1 and args.student != '':
    print("Student partial '{}' is not unique. Add characters or specify blank for all students".format(args.student))
    #TODO loop through the matches
    sys.exit(1)

  # Either have one or all students now, so figure out which assignment.
  assignments = fetch_assignments(args.assignment, cur)
  numAssignments = len(assignments)

  if numAssignments == 0:
    print("No assignment matching '{}'. Use grader-query assignments to see assignment log.".format(args.assignment))
    sys.exit(1)
    
  elif numAssignments > 1:
    print("Assignment partial '{}' is not unique. Add characters".format(args.student))
    #TODO loop through the matches
    sys.exit(1)

  # Now execute the query
  for student in students:
      set_grade(student, assignments[0], args.points, cur)

  #TODO implement update option http://stackoverflow.com/questions/3634984/insert-if-not-exists-else-update#3635038






