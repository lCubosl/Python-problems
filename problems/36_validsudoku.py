# 36. Valid Sudoku
#  

board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

def valid_in_row(row, num):
  return str(num) not in board[row]

def valid_in_col(col, num):
  return all(board[row][col] != str(num) for row in range(9))

def valid_in_square(row, col, num):
  row_start = (row // 3) * 3
  col_start = (col // 3) * 3
  for row_n in range(row_start, row_start + 3):
    for col_n in range(col_start, col_start + 3):
      if board[row_n][col_n] == str(num):
        return False
  return True

def is_valid(board):
  for row in range(9):
    for col in range(9):
      num = str(board[row][col])
      if num != ".":
        board[row][col] = "."
        if not valid_in_row(row, num) or not valid_in_col(col, num) or not valid_in_square(row, col, num):
          return False
        board[row][col] = num     
  return True

# def is_valid(empty, num):
#   row, col = empty
#   row_check = valid_in_row(row, num)
#   col_check = valid_in_col(col, num)
#   sqr_check = valid_in_square(row, col, num)
#   return all([row_check, col_check, sqr_check])

# print(valid_in_row(0,4))
# print(valid_in_col(0,3))
# print(valid_in_square(0,0,7))
print(is_valid(board))
