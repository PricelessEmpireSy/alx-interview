#!/usr/bin/python3
"""Solves the N-queens puzzle.
Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.
Example:
    $ ./0-nqueens.py N
N must be an integer greater than or equal to 4.
Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.
Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""

import sys


def is_safe(board, row, col, N):
    """Function to check if placing a queen at a specific position is safe"""
    for i in range(row):
        """Check if there's a queen in the same column or in the diagonal"""
        if board[i] == col or abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(board, row, N):
    """Function to solve the N Queens problem using backtracking"""
    if row == N:
        """If all N rows are filled, we found a solution, print it"""
        print([[i, board[i]] for i in range(N)])
        return

    for col in range(N):
        """Try placing the queen in each column of the current row"""
        if is_safe(board, row, col, N):
            """If it's safe, mark the position and move to the next row"""
            board[row] = col
            solve_nqueens(board, row + 1, N)


def nqueens(N):
    """Main function to handle input and call the solving function"""
    if not isinstance(N, int):
        """Input validation"""
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    """Create an array to represent the board.
    -1 means no queen in that row."""
    board = [-1] * N
    solve_nqueens(board, 0, N)


if __name__ == "__main__":
    """Check if the number of arguments is correct"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
