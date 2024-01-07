import tkinter as tk
import random

class WordPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Puzzle Game")

        # List of words for the puzzle
        self.words = ["python", "puzzle", "tkinter", "programming", "coding", "challenge", "game"]

        # Randomly choose a word for the puzzle
        self.current_word = random.choice(self.words)
        self.shuffled_word = self.shuffle_word(self.current_word)

        # Variables for input and display
        self.input_var = tk.StringVar()
        self.display_var = tk.StringVar()
        self.display_var.set(self.shuffled_word)

        # Input field and display label
        entry = tk.Entry(root, textvariable=self.input_var, font=("Helvetica", 14))
        entry.pack(pady=10)

        tk.Label(root, textvariable=self.display_var, font=("Helvetica", 18, "bold")).pack()

        # Submit button
        tk.Button(root, text="Submit", command=self.check_answer, font=("Helvetica", 14)).pack(pady=10)

        # Instructions label
        tk.Label(root, text="Unscramble the letters to form a word!", font=("Helvetica", 12)).pack()

    def shuffle_word(self, word):
        """
        Shuffle the letters of a word.
        """
        word_list = list(word)
        random.shuffle(word_list)
        return ''.join(word_list)

    def check_answer(self):
        """
        Check if the entered word is correct.
        """
        user_input = self.input_var.get().lower()

        if user_input == self.current_word:
            self.display_var.set("Correct! Next word:")
            self.next_word()
        else:
            self.display_var.set("Incorrect. Try again.")

    def next_word(self):
        """
        Load the next word for the puzzle.
        """
        self.current_word = random.choice(self.words)
        self.shuffled_word = self.shuffle_word(self.current_word)
        self.display_var.set(self.shuffled_word)
        self.input_var.set("")  # Clear the input field

if __name__ == "__main__":
    root = tk.Tk()
    game = WordPuzzleGame(root)
    root.mainloop()
