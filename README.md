
# To-Do List Application: Test Cases Documentation

### Table of Contents:
1. [Introduction](#introduction)
2. [Test Strategy](#test-strategy)
3. [Test Cases](#test-cases)
    - [Add Task Tests](#add-task-tests)
    - [Complete Task Tests](#complete-task-tests)
    - [Delete Task Tests](#delete-task-tests)
4. [Testing Techniques](#testing-techniques)
    - [Boundary Testing](#boundary-testing)
    - [Equivalence Partitioning](#equivalence-partitioning)
    - [State Transition Testing](#state-transition-testing)


---

## Introduction

This document outlines the test cases for the **To-Do List Application** developed using a **Test-Driven Development (TDD)** approach. The application allows users to add tasks, mark tasks as complete, and delete tasks. Each feature has been tested using various testing techniques to ensure robustness and correctness.

---

## Test Strategy

The following test strategy was employed:
- **Test-Driven Development (TDD)**: Tests are written before implementing each feature.
- **Automated Testing**: Tests are automated using Python's `unittest` module.
- **Boundary Testing**: Tests the behavior of the system at the boundary limits of input values.
- **Equivalence Partitioning**: Tests various equivalence classes of input values.
- **State Transition Testing**: Tests the state changes of tasks in the system (e.g., from "active" to "completed").

---

## Test Cases

| Test Case ID | Description                              |
|--------------|------------------------------------------|
| TC001        | Add Task with valid input                |
| TC002        | Add Task with invalid input (empty name) |
| TC003        | Add Task with maximum length             |
| TC004        | Add Task with special characters         |
| TC005        | Mark Task as complete                    |
| TC006        | Mark already completed task              |
| TC007        | Delete Task                              |
| TC008        | Delete Task with invalid index           |
| TC009        | Delete a completed task                  |
---

### Add Task Tests

| Test Case ID | Description                              | Input                          | Expected Output                 |
|--------------|------------------------------------------|--------------------------------|---------------------------------|
| TC001        | Add Task with valid input                | Task Name: "Buy groceries"     | Task added successfully         |
| TC002        | Add Task with invalid input (empty name) | Task Name: ""                  | Error raised (ValueError)       |
| TC003        | Add Task with maximum length             | Task Name: "A" * 50            | Task added successfully         |
| TC004        | Add Task with special characters         | Task Name: "Buy milk @ store"  | Task added successfully         |

#### **Implementation**:

```python
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
```

### Complete Task Tests

| Test Case ID | Description                              | Input                          | Expected Output                 |
|--------------|------------------------------------------|--------------------------------|---------------------------------|
| TC005        | Mark Task as complete                    | Task Index: 0                  | Task marked as complete         |
| TC006        | Mark already completed task              | Task Index: 0 (already done)   | Task remains completed          |
#### **Implementation**:

```python
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
```

### Delete Task Tests

| Test Case ID | Description                              | Input                          | Expected Output                 |
|--------------|------------------------------------------|--------------------------------|---------------------------------|
| TC007        | Delete Task                              | Task Index: 0                  | Task deleted successfully       |
| TC008        | Delete Task with invalid index           | Task Index: 1 (out of bounds)  | Error raised (IndexError)       |

#### **Implementation**:

```python
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
```

---

## Testing Techniques

### Boundary Testing

Boundary testing was applied to validate task names with maximum and minimum lengths.

| Test Case ID | Description                                  | Input                            | Expected Output              |
|--------------|----------------------------------------------|----------------------------------|------------------------------|
| TC003        | Add Task with maximum length                 | Task Name: "A" * 50              | Task added successfully       |
| TC002        | Add Task with empty name                     | Task Name: ""                    | Error raised (ValueError)     | 

#### **Implementation**:

```python
def test_add_max_length_task(self):
    todo_list = ToDoList()
    long_name = "A" * 50
    todo_list.add_task(long_name)
    self.assertEqual(todo_list.tasks[0].name, long_name)

def test_add_empty_task(self):
    todo_list = ToDoList()
    with self.assertRaises(ValueError):
        todo_list.add_task("")
```

---

### Equivalence Partitioning

Equivalence partitioning was used to test valid and invalid input types, such as names with special characters or whitespaces.

| Test Case ID | Description                                  | Input                            | Expected Output              | 
|--------------|----------------------------------------------|----------------------------------|------------------------------|
| TC004        | Add Task with special characters             | Task Name: "Buy milk @ store"    | Task added successfully       | 
| TC002        | Add Task with only whitespaces (invalid)     | Task Name: "   "                 | Error raised (ValueError)     | 

#### **Implementation**:

```python
def test_add_special_characters_task(self):
    todo_list = ToDoList()
    todo_list.add_task("Buy milk @ store")
    self.assertEqual(todo_list.tasks[0].name, "Buy milk @ store")

def test_add_whitespace_task(self):
    todo_list = ToDoList()
    with self.assertRaises(ValueError):
        todo_list.add_task("   ")  # Whitespaces should be invalid
```

---

### State Transition Testing

State transition testing was used to validate the transition of tasks from **active** to **completed**, and from **completed** to **deleted**.

| Test Case ID | Description                                  | Input                            | Expected Output              | 
|--------------|----------------------------------------------|----------------------------------|------------------------------|
| TC005        | Transition task from active to completed     | Task Index: 0                    | Task marked as completed      |
| TC009        | Delete a completed task                      | Task Index: 0                    | Task deleted successfully     | 

#### **Implementation**:

```python
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
```
