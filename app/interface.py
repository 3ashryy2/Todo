from app.todo_list import ToDoList

class ToDoAppUI:
    """Command-line interface for interacting with the To-Do List."""

    def __init__(self):
        self.todo_list = ToDoList()

    def show_menu(self):
        """Display the available actions to the user."""
        print("\n1. Add Task\n2. Mark Task Complete\n3. Delete Task\n4. List Tasks\n5. Exit")

    def run(self):
        """Main loop for running the command-line interface."""
        while True:
            self.show_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                task_name = input("Enter task description: ")
                self.todo_list.add_task(task_name)
                print(f"Task '{task_name}' added.")
            elif choice == '2':
                task_index = int(input("Enter task number to mark complete: ")) - 1
                try:
                    self.todo_list.complete_task(task_index)
                    print("Task marked as complete.")
                except IndexError:
                    print("Invalid task number.")
            elif choice == '3':
                task_index = int(input("Enter task number to delete: ")) - 1
                try:
                    self.todo_list.delete_task(task_index)
                    print("Task deleted.")
                except IndexError:
                    print("Invalid task number.")
            elif choice == '4':
                tasks = self.todo_list.list_tasks()
                if tasks:
                    print("\nTasks:")
                    for i, task in enumerate(tasks, start=1):
                        print(f"{i}. {task}")
                else:
                    print("No tasks available.")
            elif choice == '5':
                print("Goodbye!")
                break
            else:
                print("Invalid choice, please try again.")
