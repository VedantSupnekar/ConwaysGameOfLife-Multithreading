'''
Vedant Supnekar (R11715927) | Project #1 | 12/01/2022

This is a Project which utilizes multiprocessing modules to implement a version of Conway's Game of Life in Python 

This program has been successfully tested on TTU's HPCC Cluster.
'''


from multiprocessing import Pool
import sys
import os.path

alive = '+'
dead = '-'

#lists used in function NodeInNextCycle
PrimeNumbers = [2, 3, 5, 7]
EvenNumbers = [2, 4, 6]


#Program used to compute neighbors of location in matrix and then store them in an array. Array is returned.
def neighbors(rowNumber, colNumber):
  result = []
  for rowAdd in range(-1, 2):
    newRow = rowNumber + rowAdd
    if newRow >= -1:
      for colAdd in range(-1, 2):
        newCol = colNumber + colAdd
        if newCol >= -1 and newCol < len(puzzle[0]) and newRow < len(puzzle):
          if newCol == colNumber and newRow == rowNumber:
            continue
          result.append(puzzle[newRow][newCol])
        elif (newRow == len(puzzle) and newCol == len(puzzle[0])):
          result.append(puzzle[0][0])
        elif (newCol == len(puzzle[0])):
          result.append(puzzle[newRow][0])
        elif (newRow == len(puzzle)):
          result.append(puzzle[0][newCol])

  return result

#Function to compute number of alive neighbors of matrix node --> needs an array of neighbors obtained from neighbors function
def numAlive(array):
  count = 0
  for i in array:
    if i == alive:
      count = count + 1

  return count


#function to figure out what given node is going to be at the next cycle
def NodeInNextCycle(rowNumber, colNumber):

  NeighborArray = neighbors(rowNumber, colNumber)  #array of neighbors of that node
  AliveNeighbors = numAlive(NeighborArray)  #number of alive neighbors that node has

  if puzzle[rowNumber][colNumber] == alive:
    if (AliveNeighbors
        in EvenNumbers):  #EvenNumbers is an list that has been defined above
      return alive
    else:
      return dead

  elif puzzle[rowNumber][colNumber] == dead:
    if (AliveNeighbors
        in PrimeNumbers):  #PrimeNumbers is an list that has been defined above
      return alive
    else:
      return dead

  else:  #if matrix has anything except - or + in it
    print("ERROR")
    exit(0)


#Creating function which will store all possible coordinates of array into a list of tuples
def PossibleNodesInMatrix(matrix):
  ListOfTuples = []
  for dx in range(len(matrix)):
    for dy in range(len(matrix[0])):
      tuple = (dx, dy)
      ListOfTuples.append(tuple)

  return ListOfTuples


#convert 1D list to 2D list (2D array)
def to_matrix(List1D, NumOfCols):
  return [List1D[i:i + NumOfCols] for i in range(0, len(List1D), NumOfCols)]


#function to overwrite puzzle matrix by contents of NewMatrix
def overwrite_matrix():
  for m in range(len(puzzle)):
    for n in range(len(puzzle[0])):
      puzzle[m][n] = NewMatrix[m][n]


#function to print matrix.
def PrintMatrix():
  for i in range(len(NewMatrix)):
    for j in range(len(NewMatrix[i])):
      print(NewMatrix[i][j], end='')
    print()


def Cloning(li1):
  li_copy = li1[:]
  return li_copy


    
#function to parse arguments of input statement
def arguments(InputStatement):
  #input statement is a list
  #also includes file name inside ImputStatement at position 0
  #pass sys.argv as input of this function in main
  ReturnList = [None] * 3
  if (len(InputStatement) == 6):  #if the thread count isnt given...
    InputStatement.append('1')  #...say that the last element of the list is 1
  for i in range(1, len(InputStatement)):
    if (InputStatement[i] == "-i"):
      InputFile = InputStatement[i + 1]
      ReturnList[0] = InputFile
    elif (InputStatement[i] == "-o"):
      OutputFile = InputStatement[i + 1]
      ReturnList[1] = OutputFile
    elif (InputStatement[i] == "-t"):
      ThreadCount = InputStatement[i + 1]
      ReturnList[2] = ThreadCount

  return ReturnList  #returning a list of arguments which include name of input file at position 1, name of output file at position 2, and thread count at position 3


if __name__ == '__main__':

  print("Project :: R11715927")

  

  ArgumentList = arguments(sys.argv)
  #take parameter as sys.argv for arguments input through command line
  #sys.argv puts all the inputs in a list.
  if os.path.exists(ArgumentList[0]): #checking if input file exists
    if os.path.exists(ArgumentList[1]): #checking if output file exists
  #taking matrix from file into a 2D list.
      with open(ArgumentList[0]) as f:
        puzzle1 = [list(line.strip()) for line in f]
      
      puzzle = ([x for x in puzzle1 if x])
          
    
      
      #possible coordinates for the given matrix
      ListPossibleCoordinates = PossibleNodesInMatrix(puzzle)
      num_process = int(ArgumentList[2])  #this is user input of number of threads
      
      #Creating Matrix of same dimensions as that of input matrix
      NewMatrix = [[None for i in range(len(puzzle[0]))]
                   for j in range(len(puzzle))]
    
      #actual parallelization process.
      for i in range(100):
        with Pool(num_process) as p:
          New1DList = p.starmap(NodeInNextCycle, ListPossibleCoordinates)
    
        NewMatrix = to_matrix(New1DList, len(puzzle[0]))
    
        #overwriting puzzle matrix by elements of the new matrix, since the functions will use the puzzle matrix with the updated values
        overwrite_matrix()
        
      original_stdout = sys.stdout  # Save a reference to the original standard output
      
      with open(ArgumentList[1], 'w') as f2:
        sys.stdout = f2  # Change the standard output to the file we created.
        PrintMatrix()
        sys.stdout = original_stdout  # Reset the standard output to its original value'''
  
    else:
      exit(0)
  else:
    exit(0)
    
    
