# You have an N by N board. Write a function that, given N, returns the
# number of possible arrangements of the board where N queens can be
# placed on the board without threatening each other, i.e. no two
# queens share the same row, column, or diagonal.


import numpy as np


def place_queen(board, queen_row):
    if queen_row in board:
        return False

    queen_col = len(board)
    for col, row in enumerate(board):
        if abs(row - queen_row) == abs(col - queen_col):
            return False
    return True


def queens_on_board(N, board = []):
    if N == len(board):
        return 1

    variations = 0
    for row in range(N):
        if place_queen(board, row):
            variations += queens_on_board(N, board + [row])
    return variations


# Driver code:
result = queens_on_board(4)
print(result)

result = queens_on_board(1)
print(result)

result = queens_on_board(2)
print(result)

result = queens_on_board(10)
print(result)