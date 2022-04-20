
def stripspace(message):
  upperlist = []
  for i in message:
    if i.isupper():
      upperlist.append(i)
  return upperlist
message = input("Enter the input")
result = stripspace(message)
print (result)
