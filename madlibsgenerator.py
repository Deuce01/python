import tkinter as tk
from tkinter import ttk, simpledialog
import random

class MadLibsGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mad Libs Generator")

        self.story_templates = [
            """
            Once upon a time, in a [adjective] [noun], there lived a [adjective] [noun].
            One day, the [noun] decided to [verb] [adverb] through the [adjective] [place].
            It was a [adjective] day, and the [noun] was feeling quite [emotion].
            Suddenly, a [noun] appeared and said, "[exclamation]!" The [noun] was amazed.
            The adventure continued as the [noun] and the [noun] [verb] into the [adjective] [place].
            The [noun] lived happily ever after in the [adjective] [noun].
            """,
            # Add more story templates here
        ]

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Mad Libs Generator")
        self.label.grid(row=0, column=0, columnspan=2, pady=10)

        self.story_text = tk.Text(self.root, wrap=tk.WORD, width=40, height=10)
        self.story_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.generate_button = ttk.Button(self.root, text="Generate Mad Libs", command=self.generate_mad_libs)
        self.generate_button.grid(row=2, column=0, pady=10)

        self.quit_button = ttk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.grid(row=2, column=1, pady=10)

    def generate_mad_libs(self):
        story_template = random.choice(self.story_templates)
        self.story_text.delete(1.0, tk.END)  # Clear previous content
        self.story_text.insert(tk.END, story_template)

        word_types = ['adjective', 'noun', 'verb', 'adverb', 'place', 'emotion', 'exclamation']

        for word_type in word_types:
            replacement = simpledialog.askstring("Mad Libs Generator", f"Enter an {word_type}: ")
            self.story_text.tag_configure(word_type, foreground='blue', font=('Arial', 10, 'bold'))
            self.story_text.insert(tk.END, f"[{word_type}]")
            self.story_text.tag_add(word_type, tk.END, f"{tk.END}-{len(word_type)+2}")
            self.story_text.insert(tk.END, f" {replacement} ")

if __name__ == "__main__":
    root = tk.Tk()
    app = MadLibsGeneratorApp(root)
    root.mainloop()
