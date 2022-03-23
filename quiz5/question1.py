import random

randomlist= []
for i in range (10):
  randomlist.insert(i, random.randint(0, 100))
print(randomlist)

mini = min(randomlist)
min_location = randomlist.index(mini)
first = randomlist[0]
randomlist.remove(mini)
randomlist.remove(first)
randomlist.insert(0,mini)
randomlist.insert(min_location,first)
print (randomlist)

randomlist.remove(mini)
min2 = min(randomlist)
min2_location = randomlist.index(min2)
second = randomlist[1]
randomlist.remove(min2)
randomlist.remove(second)
randomlist.insert(0,min2)
randomlist.insert(min_location,second)
randomlist.insert(0,mini)
print (randomlist)


