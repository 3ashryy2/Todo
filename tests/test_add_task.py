import unittest
from app.todo_list import ToDoList



class TestToDoList(unittest.TestCase):
    def test_add_valid_task(self):
        todo_list = ToDoList()
        todo_list.add_task("Buy groceries")
        self.assertEqual(len(todo_list.tasks), 1)
        self.assertEqual(todo_list.tasks[0].name, "Buy groceries")

    def test_add_empty_task(self):
        todo_list = ToDoList()
        with self.assertRaises(ValueError):
            todo_list.add_task("")

    def test_add_max_length_task(self):
        todo_list = ToDoList()
        long_name = "A" * 50
        todo_list.add_task(long_name)
        self.assertEqual(todo_list.tasks[0].name, long_name)

    def test_add_special_characters_task(self):
        todo_list = ToDoList()
        todo_list.add_task("Buy milk @ store")
        self.assertEqual(todo_list.tasks[0].name, "Buy milk @ store")