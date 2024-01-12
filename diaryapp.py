import os
import datetime
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog  

def create_diary():
    if not os.path.exists("diary.txt"):
        with open("diary.txt", "w"):
            pass

def add_entry(entry):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as diary_file:
        diary_file.write(f"{timestamp}\n{entry}\n\n")

def view_entries(date=None):
    entries = []
    with open("diary.txt", "r") as diary_file:
        lines = diary_file.readlines()
        for i in range(0, len(lines), 3):
            timestamp = lines[i].strip()
            entry_date = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S").date()
            if date is None or entry_date == date:
                entry_text = lines[i + 1].strip()
                entries.append(f"{timestamp}\n{entry_text}\n")

    return entries

def save_entries(entries):
    with open("diary.txt", "w") as diary_file:
        diary_file.writelines(entries)

def delete_entry(index):
    entries = view_entries()
    if 0 <= index < len(entries):
        del entries[index:index + 3]
        save_entries(entries)
        messagebox.showinfo("Diary", "Entry deleted successfully.")
    else:
        messagebox.showwarning("Diary", "Invalid entry index.")

class DiaryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Diary App")
        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self.root, width=40, height=10)
        self.text_area.pack(padx=10, pady=10)

        self.add_button = tk.Button(self.root, text="Add Entry", command=self.add_entry)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.view_button = tk.Button(self.root, text="View Entries", command=self.view_entries)
        self.view_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(self.root, text="Delete Entry", command=self.delete_entry)
        self.delete_button.pack(side=tk.LEFT, padx=10)

    def add_entry(self):
        entry_text = self.text_area.get("1.0", tk.END).strip()
        if entry_text:
            add_entry(entry_text)
            messagebox.showinfo("Diary", "Entry added successfully.")
        else:
            messagebox.showwarning("Diary", "Please enter a diary entry.")

    def view_entries(self):
        date_str = simpledialog.askstring("Diary", "Enter date (YYYY-MM-DD) or leave blank for all entries:")
        try:
            if date_str:
                date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
            else:
                date = None

            entries = view_entries(date)
            if entries:
                result = "\n".join(entries)
                messagebox.showinfo("Diary Entries", result)
            else:
                messagebox.showinfo("Diary Entries", "No entries found.")
        except ValueError:
            messagebox.showwarning("Diary", "Invalid date format. Please use YYYY-MM-DD.")

    def delete_entry(self):
        index_str = simpledialog.askstring("Diary", "Enter the index of the entry to delete:")
        try:
            index = int(index_str)
            delete_entry(index)
        except (ValueError, TypeError):
            messagebox.showwarning("Diary", "Invalid index. Please enter a valid numeric index.")

if __name__ == "__main__":
    create_diary()

    root = tk.Tk()
    app = DiaryApp(root)
    root.mainloop()
