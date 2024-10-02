from app.task import Task

class ToDoList:
    """Manages a list of tasks, including adding, completing, and deleting tasks."""

    def __init__(self):
        self.tasks = []

    def add_task(self, name: str):
        """Add a task to the to-do list."""
        task = Task(name)
        self.tasks.append(task)

    def complete_task(self, index: int):
        """Mark a task as complete based on the index."""
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index.")
        self.tasks[index].mark_completed()

    def delete_task(self, index: int):
        """Delete a task from the list based on the index."""
        if index < 0 or index >= len(self.tasks):
            raise IndexError("Invalid task index.")
        self.tasks.pop(index)

    def list_tasks(self):
        """Return a list of all tasks with their statuses."""
        return [str(task) for task in self.tasks]
