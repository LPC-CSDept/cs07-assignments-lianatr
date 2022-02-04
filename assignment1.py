num = input("Enter the number of males in your class ")
nam = input("Enter the number of females in your class ")
sum = int(num) + int(nam)
print("The total number of students in your class is {0}".format(sum))
fpe = int(nam)/sum
mpe = int(num)/sum
print("The percentage of female students in your class is {0:.2%}".format(fpe))
print("The percentage of male students in your class is {0:.2%}".format(mpe))