import random

N = 20
randomlist = []
for i in range(N):
    randomlist.insert(i, random.randint(0, 10))
randomlist.sort()
print(randomlist)
input_remove = int(input("input the number you wish to remove"))
occurrences = randomlist.count(input_remove)
for i in range(occurrences):
    try:
        randomlist.remove(input_remove)
    except ValueError:
        print("There is no value,{0}, in this list", input_remove)
for v in randomlist:
    print(v, end=' ')
