N = int(input("how many students? "))
M = int(input("how many scores per student? "))
matrix = []
scorelist= []

for i in range (N):
  studentlist = []
  students = input("enter name of student ")
  studentlist.append(students)
  for v in range (M):
    scores = int(input("enter their scores ")) 
    scorelist.append(scores)
  matrix.append(scorelist)
  
print (matrix)

for x in range (N):
  studentsum = 0
  for j in range(M):
    studentsum += matrix[x][j]
    studentname = (studentlist[x])
    print ("{0} has a total score of {1} ".format(studentname, studentsum))
    studentavg = (studentsum/M)
    print ("{0} has an average of {1}".format(studentname,studentavg))

for x in range (N):
  scoresum = 0
  for j in range(M):
    scoresum += matrix[x][j]
    subjectnum = (scorelist[x])
    print ("{0} has a total score of {1} ",format (subjectnum, scoresum))
    scoreavg = (scoresum/M)
    print ("{0} has an average of {1}", format(subjectnum,scoreavg))
    