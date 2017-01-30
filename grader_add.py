
def add_student(cur):
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
  cur.execute(sql)
  
  return True



def add_assignment(cur):
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
  cur.execute(sql)
  
  return True

  

def add_tag(cur):
  #TODO implement this. Should be similar to the other two.
  pass



def add_command(args, cur):
  if args.item == 'student':
    add_student(cur)
    while args.multiple:
      args.multiple = add_student(cur)
  
  elif args.item == 'assignment':
    add_assignment(cur)
    while args.multiple:
      args.multiple = add_assignment(cur)
  
  elif args.item == 'tag':
    add_tag(cur)
    while args.multiple:
      args.multiple = add_tag(cur)













