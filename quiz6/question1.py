namelist = []
IDList = []
scorematrix = []

def getInput():
  studentnum = int(input("How many students would you like inputted?"))
  scorenum = int(input("How many scores would you like inputted for each student?"))
  for i in range (studentnum):
    namelist.append(input("enter name of student "))
    # IDList.appened(input("enter ID number of student"))
	# Error : Wrong method name 
    IDList.append(input("enter ID number of student"))
    studentscore= []
    for v in range (scorenum):
      studentscore.append(input("enter score {0} of student"))
    scorematrix.append(studentscore)
                          
  # return namelist, IDList, scorelist
  # ERROR: not defined scorelist. Did you mean scorematrix?
  return namelist, IDList, scorematrix
  
def FindHighestScore():
	# scorematrix should be sent to this function from main
  highestscore = max(scorematrix)
  highestLocation = index(highestscore)
  indexPersonHighest = (highestLocation)//(scorenum)
  HighestScoreName = (namelist[indexPersonHighest])
  return highestscore, HighestScoreName

def FindLowest():
	# scorematrix should be sent to this function from main
  LowestScore = min(scorematrix)
  LowestLocation = index(LowestScore)
  indexPersonLowest = (LowestLocation)//(scorenum)
  LowestScoreName = (namelist[indexPersonLowest])
  return LowestScore, LowestScoreName

def FindTotal():
	# Not defined studentnum
	# studentnum should be sent as a parameter
  for i in range (studentnum):
    studentsum = 0
    for v in range(scorenum):
      studentsum += matrix[i][v]
      studentname = (studentlist[i])
      studentavg = (studentsum/scorenum)
  return studentavg,studentsum


def PrintAll():
	# Not defined scorenum
	# scorenum should be sent as a parameter
  for i in range (scorenum):
    studentscore = []
    for v in scorematrix[i]:
      studentscore+= (v)
    
    

getInput()
PrintAll()
low = FindLowest()
high = FindHighest()

print("highest score: ", high)
print("lowest score: ", low)
    
    
    
