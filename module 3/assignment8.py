number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

low = 0
mid = 0
high = 0

if (number1>number2 and number1>number3):
  high = number1
  if(number2>number3):
    mid = number2
    low = number3
  else:
    low = number2
    mid = number3
elif (number2>number1 and number2>number3):
  high = number2
  if(number1>number3):
    mid = number1
    low = number3
  else:
    low = number1
    mid = number3
else:
  high = number3
  if(number1>number2):
    mid = number1
    low = number2
  else:
    low = number1
    mid = number2

print (low,mid,high)
