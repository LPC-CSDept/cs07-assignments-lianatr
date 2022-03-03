import random
flag = 1
prev_num = random.randint(0,100)
while (flag):
  cnum = random.randint(0,99)
  print ("the previous number is {0} and the next number is {1}".format(prev_num, cnum))
  if (cnum >= prev_num):
   print ("the next number, {1}, is greater than {0}, therefore, the loop will stop".format(prev_num,cnum))
  flag = 0