def getInput():
  namelist = []
  IDList = []
  scorematrix = []
  studentnum = int(input("How many students would you like inputted?"))
  scorenum = int(input("How many scores would you like inputted for each student?"))
  for i in range (studentnum):
    namelist.append(input("enter name of student ", i))
    IDList.appened(input("enter ID number of student", i))
    studentscore= []
    for v in range (scorenum):
      studentscore.append(input("enter score {0} of student", v))
    scorematrix.append(studentscore)
                          
  return namelist, IDList, scorelist
  
def FindHighestScore():
  highestscore = max(namelist)
  highestLocation = index(highestscore)
  indexPersonHighest = (highestLocation)//(scorenum)
  HighestScoreName = (namelist[indexPersonHighest])
  return highestscore, HighestScoreName
  

def FindLowest():
  LowestScore = min(namelist)
  LowestLocation = index(LowestScore)
  indexPersonLowest = (LowestLocation)//(scorenum)
  LowestScoreName = (namelist[indexPersonLowest])
  return LowestScore, LowestScoreName

def FindTotal():
  for i in range(studentnum):
    studentsum = 0
    for v in range(M):
      studentsum += matrix[i][v]
      studentname = (studentlist[i])
      studentavg = (studentsum/M)
 return studentavg,studentsum

def FindAvg():
  
    


def PrintAll():
  






    
    
    