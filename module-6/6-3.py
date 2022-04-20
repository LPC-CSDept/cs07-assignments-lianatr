isspace = lambda c: c == " "
def mystrip(message):
  striplist= []
  for i in message:
    if i.isspace():
      striplist.append(i)
  return striplist
message = input("enter string")
result = mystrip(message)
print(result)