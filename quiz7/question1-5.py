#1
import xlrd
from functools import reduce

wb = xlrd.open_workbook('quiz7/students.xls')
ws = wb.sheet_by_index(0)

header = []
id = []
names = []
scores = []

for i in range(ws.ncols-3):
  header.append(ws.row_values(0)[i])

for j in range(1, ws.nrows):
  id.append(ws.row_values(j)[0])
  names.append(ws.row_values(j)[1])
  scores_list = []
  for p in range(2, ws.ncols):
    scores_list.append(ws.row_values(j)[p])
  scores.append(scores_list)

#2
dictionaries = zip(id, names, scores)
list1 = []
for k in dictionaries:
  dict1 = dict(zip(header, k))
  list1.append(dict1)
print(list1)

#3
for value in filter(lambda x: sum(x['Scores']) > 350, list1):
  print(value)

#4
for n in range(ws.nrows-1):
  print(list1[n]['ID'], list1[n]['Name'], reduce(lambda a, b: a + b, list1[n]['Scores']))
#5
n = 0
for value in map(lambda x: 10000000 + x['ID'], list1):
  print(value, list1[n]['Name'], reduce(lambda a, b: a + b, list1[n]['Scores']))
  n += 1 