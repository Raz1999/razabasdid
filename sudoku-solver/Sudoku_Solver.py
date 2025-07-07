# Sudoku Solver using backtracking
# Author : Raz Abasdid

def is_valid (board, row, col, num):
  for i in range (9):
    if board[row][i] == num or board[col][i] == num:
      return False

  box_start_col = 3 * (col // 3)
  box_start_row = 3 * (row // 3)

  for i in range (3):
    for j in range (3):
      if board[box_start_row + i][box_start_col + j] == num:
        return False

  return True

def Sudoku_solve (board):
  for row in range(9):
    for col in range(9):
      if board[row][col] == 0
        for num in range(1,10):
          if is_valid(board, row, col, num):
            board[row][col] = num
            if Sudoku_solve(board):
              return True
            board[row][col] = 0
        return False
  return True



def print_board (board):
  for i in range (9):
    line = ""
    for j in range (9):
      line += str(board[i][j]) + ""
      if (j + 1) % 3 == 0 and j < 8:
        line += "|"
    print (line)
    if (i + 1) % 3 == 0 and i < 8:
      print("-" * 21)




