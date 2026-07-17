N = 8
board = [[0 for _ in range(N)] for _ in range(N)]
def is_safe(board, row, col):
    # Check left side of the current row
    for i in range(col):
        if board[row][i] == 1:
            return False
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1
    i, j = row, col
    while i < N and j >= 0:
        if board[i][j] == 1:
            return False
        i += 1
        j -= 1
    return True
def solve(board, col):
    if col >= N:
        return True
    for row in range(N):
        if is_safe(board, row, col):
            board[row][col] = 1

            if solve(board, col + 1):
                return True
            board[row][col] = 0
    return False
def print_board(board):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
if solve(board, 0):
    print("Solution:")
    print_board(board)
else:
    print("No solution exists.")