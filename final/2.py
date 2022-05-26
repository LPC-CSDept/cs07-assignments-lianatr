import random
def generateRandomNumbers ():
  randomNumbers = []
  for i in range(0, 10):
    randomNumbers.append(random.randint(0,4))
  return randomNumbers

def occuredNumbers (randomNumbers):
  occured = {'0': 0, '1': 0, '2': 0, '3': 0, '4': 0}
  for i in randomNumbers:
    occured[str(i)] += 1
  return occured

def findMaxValue (occured):
  MaxValue = 0
  for num in occured:
    if occured[num] > MaxValue:
      MaxValue = occured[num]
      best = { "number": num, "occured": occured[num] }
  return best

def printAnswer (best):
  print('Answer: ' + str(best["number"]) + ' (' + str(best["occured"]) + ' times occured)')
  
randomNumberList = generateRandomNumbers()
print(randomNumberList)
occured = occuredNumbers(randomNumberList)
MaxValue = findMaxValue(occured)
printAnswer(MaxValue)