i = 0
num = int(input("input your number "))

while (i < 2):
  num = int(input("input your number "))
  if (num % 2 == 0):
    i = i + 1
    print(num)
  else:
    if (i > 0):
      i = i - 1