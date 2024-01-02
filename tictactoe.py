import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"

        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(root, text="", font=('normal', 20), width=5, height=2,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, i, j):
        if not self.buttons[i][j]["text"]:
            self.buttons[i][j]["text"] = self.current_player
            if self.check_winner(i, j):
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Draw", "It's a draw!")
                self.reset_game()
            else:
                self.toggle_player()

    def check_winner(self, row, col):
        # Check row
        if all(self.buttons[row][j]["text"] == self.current_player for j in range(3)):
            return True

        # Check column
        if all(self.buttons[i][col]["text"] == self.current_player for i in range(3)):
            return True

        # Check diagonals
        if row == col and all(self.buttons[i][i]["text"] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.buttons[i][2 - i]["text"] == self.current_player for i in range(3)):
            return True

        return False

    def check_draw(self):
        return all(self.buttons[i][j]["text"] for i in range(3) for j in range(3))

    def toggle_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
