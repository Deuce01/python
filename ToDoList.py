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


def main():
    todo_list = TodoList()

    while True:
        print("\n==== ToDo List ====")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            index = int(input("Enter task number to mark as completed: ")) - 1
            todo_list.mark_task_as_completed(index)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            index = int(input("Enter task number to delete: ")) - 1
            todo_list.delete_task(index)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
