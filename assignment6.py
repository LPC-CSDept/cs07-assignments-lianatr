import random
number1 = random.randint(0,100)
number2 = random.randint(0,100)
number3 = random.randint(0,100)
lowest = 0
print (number1,number2,number3)

if (number1<number2 and number1<number3):
  lowest = number1
else:
  if (number2<number1 and number2<number3):
    lowest = number2
  else:
    lowest = number3 
print ("The smallest number is",lowest)