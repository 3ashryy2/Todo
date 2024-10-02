
class Task:
    """Represents a single task in the to-do list."""

    def __init__(self, name: str):
        if not name.strip():
            raise ValueError("Task name cannot be empty.")
        self.name = name
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        """String representation of the task with its status."""
        status = "Completed" if self.completed else "Active"
        return f"{self.name} [{status}]"
