int = input("insert word here ")
p = 0
x = 0

while (int.find('stop') == -1):
  idx = int.find('p')
  if (idx > -1):
    x = int.count('p')
    p = x + p
  int = input("insert word here ")
print(p)