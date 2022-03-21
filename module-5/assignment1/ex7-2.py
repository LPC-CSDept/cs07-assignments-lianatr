values = [10, 5, 20, 0, 40, 45, 50]
summation = 0

for i in range(len(values)):
    summation += values[i]
    average = summation / len(values)

print("The distance from the average between these values are:")
Distance = [abs(i - round(average, 2)) for i in values]
print(Distance)
