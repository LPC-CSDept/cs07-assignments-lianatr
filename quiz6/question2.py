list1 = []
list2 = []

findeven = lambda c : c%2 == 0
def getmerged(list1,list2):
  # new1 = []
  # new2 = []
  # final = []
  for i in list1:
    if (findeven(i)):
      yield (i)
      # final.append(i)
  for i in list2:
    if (findeven(i)):
      yield (i)
      # final.append(i)
  # final = new1 + new2
  # for i in final:
    # yield (i)

n = int(input("how many values in list 1? "))
m = int(input("how many values in list 2? "))

for i in range (n):
  list1.append(int(input("enter values in list 1: ")))
for i in range (m):
  list2.append(int(input("enter values in list 2: ")))

result = getmerged(list1, list2)
print ("the values that are not even numbers are:")
for n in result:
  print (n, end=" ")