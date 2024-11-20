# Sudoku Solver & Player

This is a Python-based Sudoku application that allows users to play, solve, and get hints for Sudoku puzzles. The project features a graphical user interface (GUI) built using Tkinter and includes options for solving, resetting, and interacting with Sudoku puzzles.

---

## Features

- **Interactive Sudoku Board**: Users can click on cells to enter their own values.
- **Validation**: Prevents users from entering numbers that violate Sudoku rules.
- **Hints**: Get hints to fill empty cells with the correct numbers.
- **Reset**: Reset the board to its initial state.
- **Solve**: Solve the entire Sudoku puzzle automatically.
- **Cool Dark-Themed GUI**: A modern, user-friendly interface with a dark mode theme.
- **Error Prevention**: Users cannot enter numbers that already exist in the Sudoku puzzle.
- **Dynamic Updates**: Hints and puzzle updates are handled interactively.

---

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/sudoku-solver.git
   cd sudoku-solver
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # On Windows, use: .venv\Scripts\activate
   ```

3. **Install required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**:
   ```bash
   python GUI.py
   ```

---

## Requirements

Make sure the following Python libraries are installed:

- **tkinter** (comes pre-installed with Python)
- **random** (built-in module)
- **os** (built-in module)

Add any additional modules if needed, e.g., for debugging.

---

## How to Play

1. Run the `GUI.py` file to launch the application.
2. Select a cell on the board to enter a number (1-9).
3. Use the **Hint** button to get suggestions for empty cells.
4. Reset the puzzle using the **Reset** button.
5. Solve the entire puzzle using the **Solve** button.

---

## File Structure

- **GUI.py**: Handles the graphical user interface for the Sudoku application.
- **solver.py**: Contains the logic for solving Sudoku puzzles using backtracking.
- **solver_text.py**: Generates random Sudoku puzzles and provides hints.

---

## Known Issues

- The GUI may not resize dynamically on smaller screens.
- Hints might not consider all possible solutions for a given board configuration.

---

## Demo



---

## Future Improvements

- Add difficulty levels to dynamically adjust puzzle complexity.
- Implement a timer to track how long the user takes to solve the puzzle.
- Improve the GUI design for better user experience.
- Add an undo/redo feature for player moves.

---

## Contributing

Contributions are welcome! Feel free to fork this repository and submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
