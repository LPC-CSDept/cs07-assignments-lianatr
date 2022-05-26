from functools import reduce
caFile = open('final/CA2021.txt')
orFile = open('final/OR2021.txt')

#question 1-1

caMale = []
caMaleNum = []
caFemale = []
caFemaleNum = []

orMale = []
orMaleNum = []
orFemale = []
orFemaleNum = []

allData = []
labels = ["state","name","gender","number"]

#question 1-2

for line in caFile:
  line = line.replace("\n","")
  line = line.split(" ")
  caMale.append(line[1])
  caMaleNum.append(line[2])
  caFemale.append(line[3])
  caFemaleNum.append(line[4])

for line in orFile:
  line = line.replace("\n","")
  line = line.split(" ")
  orMale.append(line[1])
  orMaleNum.append(line[2])
  orFemale.append(line[3])
  orFemaleNum.append(line[4])

for i in range(len(orMale)):
  data = ["OR"]+[orMale[i]]+["Male"]+[orMaleNum[i]]
  allData.append(dict(zip(labels,data)))
  
for i in range(len(orFemale)):
  data = ["OR"]+[orFemale[i]]+["Female"]+[orFemaleNum[i]]
  allData.append(dict(zip(labels,data)))
  
for i in range(len(caMale)):
  data = ["OR"]+[caMale[i]]+["Male"]+[caMaleNum[i]]
  allData.append(dict(zip(labels,data)))
  
for i in range(len(caFemale)):
  data = ["OR"]+[caFemale[i]]+["Female"]+[caFemaleNum[i]]
  allData.append(dict(zip(labels,data)))

#question 1-3

caMales = list(filter(lambda x: x['state'] == 'CA' and x['gender'] == 'Male', allData))
caMales = sorted(caMales, key=lambda x: x["number"], reverse=True)

for people in caMales[:10]:
  print(people)

print("-------------------------------------")

orFemales = list(filter(lambda x: x['state'] == 'OR' and x['gender'] == 'Female', allData))

orFemalesE = list(filter(lambda x: x["name"][0]=="E", orFemales))
orFemalesE = sorted(orFemalesE, key=lambda x: x["number"], reverse=True)

for people in orFemalesE[:10]:
  print(people)


orFemales = list(map(lambda x:int(x["number"].replace(",","")),orFemales))
sumnum = lambda x,y: x+y('number')
totalNumber = reduce(sumnum, orFemales, 0)
print(totalNumber)