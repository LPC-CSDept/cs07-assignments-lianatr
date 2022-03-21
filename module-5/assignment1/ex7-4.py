number = [5,20,30,35,50]

add_value = int(input("insert value here"))

for i in range (len(number)):
    if (number[i] > add_value):
        number.insert(i, add_value)
        break
else:
    number.insert(i+1,add_value)
  
for v in number:
    print (v, end=' ')