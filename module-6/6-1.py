def sumProduct(list1,list2):
  productlist = []
  for i in range (n):
    productlist.append(list1[i]*list2[i])
  return sum(productlist)

list1 = []
list2 = []
n = int(input("how many values each in list 1 and list 2? "))

for i in range (n):
  list1.append(int(input("enter values in list 1: ")))
  list2.append(int(input("enter values in list 2: ")))

print ("list 1: ",list1)
print ("list 2: ",list2)

result = sumProduct(list1,list2)
print (result)