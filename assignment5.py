import random

number1 = random.randint(0, 100)
number2 = random.randint(0, 100)
number3 = random.randint(0, 100)
print(number1, number2, number3)
if (number1 == number2 and number2 == number3):
    print("all values are equal")
else:
    if (number1 == number2):
        print("Numbers 1 and 2 are equal but distinct from number 3")
    elif (number2 == number3):
        print("numbers 2 and 3 are equal but distinct from number 1")
    elif (number1 == number3):
        print("numbers 1 and 3 are equal but distict from number 1")
    else:
        print("all numbers are distinct")
