import unittest
from app.todo_list import ToDoList


class TestToDoList(unittest.TestCase):
    def test_active_to_completed_state(self):
        todo_list = ToDoList()
        todo_list.add_task("Exercise")
        todo_list.complete_task(0)
        self.assertTrue(todo_list.tasks[0].completed)

    def test_delete_completed_task(self):
        todo_list = ToDoList()
        todo_list.add_task("Read a book")
        todo_list.complete_task(0)
        todo_list.delete_task(0)
        self.assertEqual(len(todo_list.tasks), 0)