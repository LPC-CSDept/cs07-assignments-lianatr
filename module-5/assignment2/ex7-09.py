first = input("enter keyword")
second = int(input("enter number of words to be inputted"))
string = []

for i in range (second):
    string.insert(0,input("enter word"))
if first in string:
    print ("true")
else:
    print ("false")