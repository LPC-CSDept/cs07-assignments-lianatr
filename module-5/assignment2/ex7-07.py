num1 = []
valuenum1 = int(input("input the number of values in list: "))

for i in range(valuenum1):
  num1.append(int(input("enter values in list 1: ")))

print (num1)

num2 = []
valuenum2 = int(input("input the number of values in list 2: "))

for v in range(valuenum2):
  num2.append(int(input("enter values in list 2: ")))

print (num2)

new_list=[]
if len(num1) < len(num2):
    new_list = num1+num2
else:
    new_list = num2+num1
print (new_list)