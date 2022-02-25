i = 0

while (i < 2):
  num = int(input("input your number "))
  print(num)
  if (num % 2 == 0):
    i = i + 1
  else:
    if (i > 0):
      i = i - 1