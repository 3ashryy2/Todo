import unittest
from app.todo_list import ToDoList


class TestToDoList(unittest.TestCase):

    def test_add_special_characters_task(self):
        todo_list = ToDoList()
        todo_list.add_task("Buy milk @ store")
        self.assertEqual(todo_list.tasks[0].name, "Buy milk @ store")

    def test_add_whitespace_task(self):
        todo_list = ToDoList()
        with self.assertRaises(ValueError):
            todo_list.add_task("   ")  # Whitespaces should be invalid