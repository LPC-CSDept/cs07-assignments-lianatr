import random
flag = 1
prev_num = 99
while (flag):
  cnum = random.randint(0,99)
  print(cnum)
  if (cnum > prev_num):
    flag = 0
  prev_num = cnum


   