import tkinter as tk

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def mark_task_as_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]["completed"] = True
        else:
            print("Invalid task index")

    def view_tasks(self):
        if self.tasks:
            for index, task in enumerate(self.tasks):
                status = "✓" if task["completed"] else " "
                print(f"{index + 1}. [{status}] {task['task']}")
        else:
            print("No tasks in the list")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("Invalid task index")

class TodoApp:
    def __init__(self, master):
        self.master = master
        self.todo_list = TodoList()

        self.task_entry = tk.Entry(master)
        self.task_entry.pack()

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.task_listbox = tk.Listbox(master)
        self.task_listbox.pack()

        self.view_tasks()

        self.mark_button = tk.Button(master, text="Mark as Completed", command=self.mark_task)
        self.mark_button.pack()

        self.delete_button = tk.Button(master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.view_tasks()

    def view_tasks(self):
        self.task_listbox.delete(0, tk.END)
        if self.todo_list.tasks:
            for task in self.todo_list.tasks:
                status = "✓" if task["completed"] else " "
                self.task_listbox.insert(tk.END, f"[{status}] {task['task']}")

    def mark_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list.mark_task_as_completed(index)
            self.view_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.todo_list.delete_task(index)
            self.view_tasks()

def main():
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
