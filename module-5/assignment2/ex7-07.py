num1 = [1,2,3,4]
num2 = [5,6,7]
new_list = []

if len(num1) < len(num2):
    new_list = num1+num2
else:
    new_list = num2+num1
print (new_list)