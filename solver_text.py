import random  # Add this import to use random functions

from solver import solve_sudoku  # Import solve_sudoku from solver.py

def generate_sudoku_puzzle(difficulty="medium"):
    # Generate the puzzle base (e.g., with empty spaces)
    base_board = [[0]*9 for _ in range(9)]  # This is just a placeholder, replace with actual puzzle generation logic.
    
    # For simplicity, we will use a predefined easy puzzle (you can improve this with a generator).
    if difficulty == "medium":
        base_board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
    
    # Solve the base puzzle to generate a valid solution
    solve_sudoku(base_board)
    
    # Remove some numbers to create the puzzle (the number of cells removed depends on difficulty)
    num_cells_to_remove = 30 if difficulty == "medium" else 40
    for _ in range(num_cells_to_remove):
        row, col = random.randint(0, 8), random.randint(0, 8)
        base_board[row][col] = 0
    
    return base_board
