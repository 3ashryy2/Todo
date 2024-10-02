import unittest
from app.todo_list import ToDoList


class TestToDoList(unittest.TestCase):
    def test_complete_task(self):
        todo_list = ToDoList()
        todo_list.add_task("Do laundry")
        todo_list.complete_task(0)
        self.assertTrue(todo_list.tasks[0].completed)

    def test_complete_already_completed_task(self):
        todo_list = ToDoList()
        todo_list.add_task("Do laundry")
        todo_list.complete_task(0)
        todo_list.complete_task(0)  # Should not cause issues
        self.assertTrue(todo_list.tasks[0].completed)