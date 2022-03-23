N = int(input("how many students? "))
M = int(input("how many scores per student? "))
matrix = []
scorelist= []
studentlist = []

for i in range (N):
    students = input("enter name of student ")
    studentlist.append(students)
    scorelist = []
    for v in range (M):
        scores = int(input("enter their scores ")) 
        scorelist.append(scores)
        print (scorelist)
    matrix.append(scorelist)

print (matrix)

for i in range (N):
  studentsum = 0
  for v in range(M):
    studentsum += matrix[i][v]
    studentname = (studentlist[i])
  print ("{0} has a total score of {1} ".format(studentname, studentsum))
  studentavg = (studentsum/M)
  print ("{0} has an average of {1}".format(studentname,studentavg))

for i in range (N):
  scoresum = 0
  for v in range(M):
    scoresum += matrix[v][i]
  print ("subject", i+1, "has a total score of",scoresum)
  scoreavg = (scoresum/M)
  print ("subject",i+1,"has an average of",scoreavg)