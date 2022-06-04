import numpy as np
import helperFunc as hf

sudoku = np.load("data/medium_puzzle.npy")
print("easy_puzzle.npy has been loaded into the variable sudoku")
sudokuNum = 8

print(sudoku[sudokuNum])

def sudoku_solver(sudoku):
  
    solved_sudoku = sudoku[sudokuNum].copy()
    new_sudoku = np.array([])
  
    for row, i in enumerate(solved_sudoku):
      for col,j in enumerate(i):
        if j == 0:
          solutions = []
          for n in hf.poss(hf.horiz(solved_sudoku,row)):
            #print("Possibilities")
            #print(poss(horiz(solved_sudoku, row)))
            #print(poss(verticle(solved_sudoku,col)))
            #print(poss(square(solved_sudoku,col,row)))
            if (n in hf.poss(hf.verticle(solved_sudoku,col))) and (n in (hf.poss(hf.square(solved_sudoku,col,row)))):
              solutions.append(n)
          if len(solutions) == 1:
            solved_sudoku[row, col] = solutions[0]
          elif len(solutions) == 0:
            if not np.any(new_sudoku):
              hf.noSolution(solved_sudoku)
              return solved_sudoku
            else:
              solved_sudoku = new_sudoku[1]
              #np.delete(new_sudoky[0])
          else:
            for i in range (0,len(solutions)):
              sol = []
              sol.append(solutions[i])
              new_sudoku = np.append(new_sudoku,sol)

    if len(new_sudoku)>0:
      chooseOp(solved_sudoku, new_sudoku)

    hf.check_Answer(solved_sudoku)
    return solved_sudoku
   
def chooseOp(sudoku,versions):
  for row, i in enumerate(sudoku):
    for col,j in enumerate(i):
      if j == 0:
        for i in range(0, len(versions)):
          sudoku[row,col] = versions[i]
          if hf.broken(sudoku):
            continue
          else:
            return sudoku
    

sudoku_solver(sudoku)
    
