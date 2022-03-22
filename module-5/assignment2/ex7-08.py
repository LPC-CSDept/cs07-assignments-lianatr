list1 = []
valuenum1 = int(input("input the number of values in list: "))

for i in range(valuenum1):
  list1.append(int(input("enter values in list 1: ")))

print (list1)

list2 = []
valuenum2 = int(input("input the number of values in list 2: "))

for v in range(valuenum2):
  list2.append(int(input("enter values in list 2: ")))

print (list2)

list3 = []

if len(list1) . len(list2):
  count = list1
else:
  count = list2

for i in range(len(count)):
  try:
    list3.append(list1[i])
  except:
    pass
  try:
    list3.append(list2[i])
  except:
    pass

print (list3)