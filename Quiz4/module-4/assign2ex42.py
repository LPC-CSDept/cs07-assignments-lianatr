import random
i = random.randint(0,100)
sum=0
while (sum<100):
  print (i)
  sum += i
  i = random.randint(0,100)
  if sum<100:
    break 
  
print ("The sum of all the numbers is", sum-i)
