def solve(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                for num in '123456789':
                    if all(num != board[i][x] and num != board[x][j] and 
                           num != board[i//3*3 + x//3][j//3*3 + x%3] for x in range(9)):
                        board[i][j] = num
                        if solve(board):
                            return True
                        board[i][j] = '.'
                return False
    return True

def print_board(board):
    for row in board:
        print(' '.join(row))

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

solve(board)
print_board(board)
