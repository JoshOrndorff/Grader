#! /usr/bin/python3

import argparse
import sqlite3
# Note: conditional imports below.

# Create the overall parser
parser = argparse.ArgumentParser(description="A simple commandline gradebook utility that stays out of your way.")
parser.add_argument('-f', '--filename', default='dbgrades.db', help="The name of the grades database file to use.")
subparsers = parser.add_subparsers(dest='command')

# Add command
addParser = subparsers.add_parser('add', help="Add student, assignment, or tag to the database")
addParser.add_argument('item', choices=['student', 'assignment', 'tag'])
addParser.add_argument('-m', '--multiple', action="store_true", help="Add several items to the database.")

# Init command
initParser = subparsers.add_parser('init', help="Initialize a new database or verify an existing one.")

# Set command
setParser = subparsers.add_parser('set', help="Set the grade for a given student and assignment")
setParser.add_argument('-u', '--update', action='store_true', help="Update a grade if it already exists.")
setParser.add_argument('student', help="Specify enough of a student name to be unique or <blank> to select all students")
setParser.add_argument('assignment', help="Specify enough of an assignment name to be unique. No all option provided.")
setParser.add_argument('points', type=int, help="How many points the student earned") #TODO change type to str when implementing % feature

#TODO Query command

#TODO Tag command

# Actually parse
args = parser.parse_args()

# Make the cursor and dispatch
with sqlite3.connect(args.filename) as connection:
  cur = connection.cursor()
  
  if args.command == 'add':
    from grader_add import *
    add_command(args, cur)
    
  elif args.command == 'init':
    from grader_init import *
    init_command(args, cur)
  
  elif args.command == 'set':
    from grader_set import *
    set_command(args, cur)
  
  elif args.command == 'query':
    print("Querying Not yet supported")
    print(args)
  
  elif args.command == 'tag':
    print("Tagging Not yet supported")
    print(args)
  
  else:
    print("Unrecoginzed command {}. Aborting.".format(args.command))
    print("Use --help for usage.")






