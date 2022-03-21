N = 5
numbers = []
summation = 0
min = 0
max = 0

for i in range(5):
	user_input = int(input('Enter your input'))
	numbers.insert(i, user_input)

min = min(numbers)
max = max(numbers)
del numbers[min]
del numbers [max]

summation += (numbers[i])
print(summation)

avg = summation/len(numbers)