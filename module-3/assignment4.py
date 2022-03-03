x = input("Enter your x coordinate ")
y = input("Enter your y coordinate ")

if ( int(x) > 0) and (int(y) > 0):
  print ("You are in the 1st Quadrant")
elif ( int(x) < 0) and (int(y) > 0):
  print ("You are in the 2nd Quadrant")
elif ( int(x) < 0) and (int(y) < 0):
  print ("You are in the 3rd Quadrant")
elif ( int(x) > 0) and (int(y) < 0):
  print ("You are in the 4th Quadrant")
