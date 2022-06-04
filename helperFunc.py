import numpy as np

def poss(nums):
  nums.sort()
  possibilities = []
  for i in range (1,10):
    if i not in nums:
      possibilities.append(i)
  return possibilities 

def horiz(sudoku, num):
  h = []
  for i in sudoku[num]:
    h.append(i)
  return h

def verticle(sudoku,num):
  v = []
  for i in sudoku:
    v.append(i[num])
  return v

def square(sudoku, num1, num2):
  rowNum = []
  rowNum.append(num2)
  if num2 % 3 == 0:
    rowNum.append(num2+1)
    rowNum.append(num2+2)
  if num2 % 3 == 1:
    rowNum.append(num2+1)
    rowNum.append(num2-1)
  if num2 % 3 == 2:
    rowNum.append(num2-2)
    rowNum.append(num2-1)
  rowNum.sort()
  
  colNum = []
  colNum.append(num1)
  if num1 % 3 == 0:
    colNum.append(num1+1)
    colNum.append(num1+2)
  if num1 % 3 == 1:
    colNum.append(num1+1)
    colNum.append(num1-1)
  if num1 % 3 == 2:
    colNum.append(num1-1)
    colNum.append(num1-2)
  colNum.sort()

  s = []
  for i in range(3):
    for j in range(3):
      s.append(sudoku[rowNum[i],colNum[j]])
  s.sort()
  return s
    

def noSolution(sudoku):
  for row, i in enumerate(sudoku):
      for col,j in enumerate(i):
        sudoku[row,col] = -1

def broken(sudoku):
  if checkRows(sudoku) or checkCols(sudoku):
      return True
  return False

def checkRows(sudoku):
  for row, i in enumerate(sudoku):
    line = []
    for i in line:
      if i != 0:
        line.append(i)
    if len(line) != len(set(line)):
      return True
  return False 

def checkCols(sudoku):
  for n in range (0,9):
    line = []
    for i in sudoku:
      if i[n] != 0:
        line.append(i[n])
    if len(line) != len(set(line)):
      return True
  return False

def check_Answer(sudoku):
  raw_answer = np.load("data/medium_solution.npy")
  answer = raw_answer[8].astype(int)
  print(answer)
  if np.array_equal(sudoku,answer):
    print("PASS")
    return True
  else:
    print("FAIL")
    print(answer)
    return False