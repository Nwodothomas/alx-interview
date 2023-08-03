#!/usr/bin/python3
"""N Queens placement on NxN chessboard"""

import sys

def generate_solutions(row, column):
    # Initialize the solution with an empty array to start placing queens row by row
    solution = [[]]

    # Iterate through each row to place queens on the chessboard
    for queen in range(row):
        solution = place_queen(queen, column, solution)
    
    return solution

def place_queen(queen, column, prev_solution):
    safe_position = []

    # Iterate through each array representing the previous queen placements
    for array in prev_solution:
        # Try placing the queen in each column of the current row
        for x in range(column):
            if is_safe(queen, x, array):
                # If the position is safe, add the new position to the safe positions list
                safe_position.append(array + [x])
    
    return safe_position

def is_safe(q, x, array):
    # Check if the queen is in the same column as any previous queen
    if x in array:
        return False
    else:
        # Check diagonally if the queen can attack any previous queen
        return all(abs(array[column] - x) != q - column for column in range(q))

def init():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Get the size of the chessboard from the command-line argument
    if sys.argv[1].isdigit():
        n = int(sys.argv[1])
    else:
        print("N must be a number")
        sys.exit(1)

    # Check if the size of the chessboard is at least 4
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    return n

def n_queens():
    # Initialize the program and get the size of the chessboard
    n = init()

    # Generate all possible solutions for placing queens on the chessboard
    solutions = generate_solutions(n, n)

    # Print the cleaned up solutions
    for array in solutions:
        clean = []
        for q, x in enumerate(array):
            clean.append([q, x])
        print(clean)

if __name__ == '__main__':
    n_queens()
