import random

i = 0
sum = 0

while (i < 10):
  num = random.randint(0,100)
  print (num)
  i = i+1
  sum += num
  if (sum >= 100):
    print ("the total, {0} is greater than 100".format(sum))
    break
else:
    print ("the total, {0}, is less than or equal to 100".format(sum))