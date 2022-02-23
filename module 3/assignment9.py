import sys
email = (input("Enter your email: "))

if (len(email)<5):
  print("Email is too short.")
  sys.exit (0)
if (len(email)>30):
  print("Email is too long.")
  sys.exit (0)
idx = email.find('@')
if (idx == -1):
  print("@ symbol required")
  sys.exit (0)
dot = email[idx:]
if ( dot.find('.') == -1):
  print("valid domain name required")
  sys.exit (0)

else:
  print ("The email address is valid")