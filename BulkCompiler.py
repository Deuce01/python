import os
import shutil
import subprocess
import tkinter as tk
from tkinter import filedialog

class JavaCompilerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Java Compiler")

        self.status_label = tk.Label(self, text="Drag a Java file here or click Browse to select.")
        self.status_label.config(font=("Arial", 14))
        self.status_label.pack(pady=20)

        self.output_folder_var = tk.StringVar()
        self.output_folder_var.set(os.getcwd())  # Default to current directory
        self.output_folder_label = tk.Label(self, text="Output Folder:")
        self.output_folder_label.pack(pady=5)
        self.output_folder_entry = tk.Entry(self, textvariable=self.output_folder_var)
        self.output_folder_entry.pack(pady=5)
        self.browse_output_folder_button = tk.Button(self, text="Browse Output Folder", command=self.browse_output_folder)
        self.browse_output_folder_button.pack(pady=5)

        self.bind("<Drop>", self.on_drop)
        self.bind("<Drop>", lambda event: event.widget.focus_set(), add="+")

        self.browse_java_button = tk.Button(self, text="Browse Java File", command=self.browse_java_file)
        self.browse_java_button.pack(pady=10)

    def on_drop(self, event):
        java_file_path = event.data
        if os.path.isfile(java_file_path) and java_file_path.endswith(".java"):
            self.compile_java_file(java_file_path)
        else:
            self.update_status("Not a valid Java file.")

    def browse_java_file(self):
        java_file_path = filedialog.askopenfilename(filetypes=[("Java files", "*.java")])
        if java_file_path:
            self.compile_java_file(java_file_path)

    def browse_output_folder(self):
        output_folder = filedialog.askdirectory()
        if output_folder:
            self.output_folder_var.set(output_folder)

    def compile_java_file(self, java_file_path):
        file_name = os.path.basename(java_file_path)
        class_name = file_name[:-5]  # Remove ".java" extension
        try:
            subprocess.run(["javac", java_file_path, "-d", self.output_folder_var.get()], check=True)
            self.update_status(f"Compiled: {file_name}")
        except subprocess.CalledProcessError:
            self.update_status(f"Failed to compile: {file_name}")
        except Exception as e:
            self.update_status(f"Error compiling: {file_name}\n{e}")

    def update_status(self, message):
        self.status_label.config(text=message)

if __name__ == "__main__":
    app = JavaCompilerApp()
    app.mainloop()
