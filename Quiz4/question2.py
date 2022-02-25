int = input("insert phrase here ")
p = 0

while (int.find('.') == -1):
  idx = int.find('p')
  if (idx > -1):
    p = p + 1
  int = input("insert phrase here ")
print(p)