#!/usr/bin/python3
# File: 101-nqueens.py
# Author: Oluwatobiloba Light
"""
Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer >= 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def is_safe(board, row, col):
    """
    Checks if placing a queen at board[row][col] is safe

    Args:
        board (list[int]): List representation of a chessboard
        row (int): Row of a chessboard
        col (int): Column of a chessboard

    Returns:
        bool: True if it is safe else false
    """
    for i in range(row):
        if board[i] == col or board[i] - col == i - row or\
                board[i] - col == row - i:
            return False
    return True


def place_queen(board, row):
    """
    Place a queen on the board

    Args:
        board (list[int]): List representation of a chessboard
        row (int): Row of a chessboard
    """
    if row == len(board):
        print_solution(board)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            board[row] = col
            place_queen(board, row+1)
            board[row] = -1


def print_solution(board):
    """
    Prints all the possible solution to the problem

    Args:
        board (list[int]): List representation of a chessboard
    """
    result = []
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row] == col:
                result.append([row, col])
    print(result)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * N
    place_queen(board, 0)
