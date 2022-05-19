isspace = lambda c: c == ' ' 
def getalnum (msg):
	for i in msg:
		if (not isspace):
		# if (not isspace(i)):
			print (i)
			yield i
# return msg
msg = input("insert message here")
res = getalnum(msg)
for v in res:
  print (v)