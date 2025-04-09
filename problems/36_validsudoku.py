# 36. Valid Sudoku
# using arrays time complexity O(81 x 1) or O(1)
# if board array was n x n, time complexity would be O(N x N x N)


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

print(is_valid(board))

def is_valid_w_sets(board):
  rows = [set() for _ in range(9)]
  cols = [set() for _ in range(9)]
  boxes = [set() for _ in range(9)]

  for r in range(9):
    for c in range(9):
      val = board[r][c]
      if val == ".":
        continue

      if val in rows[r]:
        return False
      rows[r].add(val)

      if val in cols[c]:
        return False
      cols[c].add(val)

      box_index = (r // 3) * 3 + (c // 3)
      if val in boxes[box_index]:
        return False
      boxes[box_index].add(val)
  
  return True

print(is_valid_w_sets(board))
