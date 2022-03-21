list1 = [10, 5, 20, 0, 40, 45, 50]
list2 = [40, 10, 5]
count = 0

for x in list2:
    for i in list1:
        if (x == i):
            count += 1

if (count == len(list2)):
    print("True")
else:
    print("False")
