import unittest
from app.todo_list import ToDoList


class TestToDoList(unittest.TestCase):
    def test_delete_task(self):
        todo_list = ToDoList()
        todo_list.add_task("Walk the dog")
        todo_list.delete_task(0)
        self.assertEqual(len(todo_list.tasks), 0)

    def test_delete_invalid_task(self):
        todo_list = ToDoList()
        todo_list.add_task("Walk the dog")
        with self.assertRaises(IndexError):
            todo_list.delete_task(1)  # Invalid index