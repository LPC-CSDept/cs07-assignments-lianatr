import random
prev_num = random.randint(0,99)
while True:
  cnum = random.randint(0,99)
  print("the previous number is {0} and the next number is {1}".format(prev_num, cnum))
  if (cnum > prev_num):
    print ("the next number, {1}, is greater than {0}, therefore, the loop will stop".format(prev_num,cnum))
    break
  else:
    print("this will not be executed")
  prev_num = cnum