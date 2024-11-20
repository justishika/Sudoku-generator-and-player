import tkinter as tk
from tkinter import messagebox, simpledialog
from solver_text import generate_sudoku_puzzle
from solver import solve_sudoku
import random


class SudokuGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Sudoku")
        self.window.configure(bg="#2E2E2E")  # Dark background
        self.board = generate_sudoku_puzzle("medium")  # Default difficulty
        self.board_state = [row[:] for row in self.board]  # To keep track of changes for Reset
        self.original_board = [row[:] for row in self.board]  # To keep track of the original puzzle
        self.buttons = []
        self.create_widgets()

    def create_widgets(self):
        self.create_board()
        self.create_controls()

    def create_board(self):
        grid_frame = tk.Frame(self.window, bg="#1E1E1E", padx=10, pady=10)
        grid_frame.grid(row=0, column=0, columnspan=9)

        for r in range(9):
            row_buttons = []
            for c in range(9):
                bg_color = "#3E3E3E" if (r // 3 + c // 3) % 2 == 0 else "#4E4E4E"
                button = tk.Button(
                    grid_frame,
                    text=str(self.board[r][c]) if self.board[r][c] != 0 else '',
                    width=5, height=2,
                    font=("Helvetica", 16),
                    bg=bg_color,
                    fg="white" if self.board[r][c] != 0 else "#A9A9A9",
                    activebackground="#5E5E5E",
                    relief="ridge",
                    command=lambda r=r, c=c: self.on_cell_click(r, c),
                    state=tk.DISABLED if self.board[r][c] != 0 else tk.NORMAL
                )
                button.grid(row=r, column=c, padx=1, pady=1, sticky="nsew")
                row_buttons.append(button)
            self.buttons.append(row_buttons)

        for i in range(9):
            grid_frame.columnconfigure(i, weight=1)
            grid_frame.rowconfigure(i, weight=1)

    def create_controls(self):
        control_frame = tk.Frame(self.window, bg="#2E2E2E")
        control_frame.grid(row=10, column=0, columnspan=9, pady=10)

        hint_button = tk.Button(
            control_frame, text="Hint", font=("Helvetica", 14), bg="#6C63FF", fg="white",
            activebackground="#4A47A3", width=10, command=self.give_hint
        )
        hint_button.grid(row=0, column=0, padx=5)

        solve_button = tk.Button(
            control_frame, text="Solve", font=("Helvetica", 14), bg="#FF6F61", fg="white",
            activebackground="#A3453D", width=10, command=self.solve_puzzle
        )
        solve_button.grid(row=0, column=1, padx=5)

        reset_button = tk.Button(
            control_frame, text="Reset", font=("Helvetica", 14), bg="#6C757D", fg="white",
            activebackground="#495057", width=10, command=self.reset_game
        )
        reset_button.grid(row=0, column=2, padx=5)

    def on_cell_click(self, row, col):
        if self.board[row][col] != 0:  # Prevent editing pre-existing numbers
            return
        value = self.board_state[row][col]
        new_value = self.get_new_value(value)
        if new_value is not None:
            if self.is_valid_move(row, col, new_value):
                self.board_state[row][col] = new_value
                self.buttons[row][col].config(text=str(new_value), fg="white")
            else:
                messagebox.showerror("Invalid Move", f"The number {new_value} is already present in the row, column, or 3x3 subgrid.")

    def get_new_value(self, current_value):
        new_value = simpledialog.askstring("Enter Value", f"Current Value: {current_value}")
        if new_value and new_value.isdigit() and 1 <= int(new_value) <= 9:
            return int(new_value)
        return None

    def is_valid_move(self, row, col, value):
        # Check row
        if value in self.board_state[row]:
            return False
        # Check column
        if value in [self.board_state[r][col] for r in range(9)]:
            return False
        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                if self.board_state[r][c] == value:
                    return False
        return True

    def give_hint(self):
        empty_cells = [(r, c) for r in range(9) for c in range(9) if self.board_state[r][c] == 0]
        if not empty_cells:
            messagebox.showinfo("Hint", "No empty cells to fill.")
            return
        r, c = random.choice(empty_cells)
        hint_value = self.board[r][c]
        self.board_state[r][c] = hint_value
        self.buttons[r][c].config(text=str(hint_value), fg="white")
        messagebox.showinfo("Hint", f"Hint: Fill ({r+1}, {c+1}) with {hint_value}")

    def reset_game(self):
        self.board_state = [row[:] for row in self.board]
        for r in range(9):
            for c in range(9):
                self.buttons[r][c].config(
                    text=str(self.board_state[r][c]) if self.board_state[r][c] != 0 else '',
                    state=tk.DISABLED if self.board[r][c] != 0 else tk.NORMAL,
                    fg="white" if self.board_state[r][c] != 0 else "#A9A9A9"
                )

    def solve_puzzle(self):
        solve_sudoku(self.board_state)
        for r in range(9):
            for c in range(9):
                self.buttons[r][c].config(text=str(self.board_state[r][c]), fg="white")

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    SudokuGUI().run()
