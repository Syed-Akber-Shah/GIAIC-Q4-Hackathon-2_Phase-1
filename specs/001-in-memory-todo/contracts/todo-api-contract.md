# API Contract: Todo Application Operations

## Overview
This document defines the interface contracts for the todo application operations. Since this is a console application, these represent the internal function interfaces that will be implemented in the todo_manager.py module.

## Task Operations

### Add Task
- **Function**: `add_task(description: str) -> int`
- **Purpose**: Creates a new task with the given description
- **Parameters**:
  - `description`: String containing the task description (required, max 250 chars)
- **Returns**: Integer representing the unique ID of the newly created task
- **Errors**:
  - Raises ValueError if description is empty
  - Raises ValueError if description exceeds 250 characters

### Get Task
- **Function**: `get_task(task_id: int) -> Optional[Task]`
- **Purpose**: Retrieves a task by its ID
- **Parameters**:
  - `task_id`: Integer representing the unique ID of the task (required)
- **Returns**: Task object if found, None otherwise
- **Errors**: None

### Get All Tasks
- **Function**: `get_all_tasks() -> List[Task]`
- **Purpose**: Retrieves all tasks in the task list
- **Parameters**: None
- **Returns**: List of all Task objects in the collection
- **Errors**: None

### Update Task
- **Function**: `update_task(task_id: int, new_description: str) -> bool`
- **Purpose**: Updates the description of an existing task
- **Parameters**:
  - `task_id`: Integer representing the unique ID of the task (required)
  - `new_description`: String containing the new task description (required, max 250 chars)
- **Returns**: Boolean indicating success (True) or failure (False)
- **Errors**:
  - Raises ValueError if new_description is empty
  - Raises ValueError if new_description exceeds 250 characters

### Mark Complete
- **Function**: `mark_complete(task_id: int) -> bool`
- **Purpose**: Marks a task as complete
- **Parameters**:
  - `task_id`: Integer representing the unique ID of the task (required)
- **Returns**: Boolean indicating success (True) or failure (False)
- **Errors**: None

### Mark Incomplete
- **Function**: `mark_incomplete(task_id: int) -> bool`
- **Purpose**: Marks a task as incomplete
- **Parameters**:
  - `task_id`: Integer representing the unique ID of the task (required)
- **Returns**: Boolean indicating success (True) or failure (False)
- **Errors**: None

### Delete Task
- **Function**: `delete_task(task_id: int) -> bool`
- **Purpose**: Removes a task from the task list
- **Parameters**:
  - `task_id`: Integer representing the unique ID of the task (required)
- **Returns**: Boolean indicating success (True) or failure (False)
- **Errors**: None

## Task Model

### Task Object
- **Attributes**:
  - `id`: Integer, unique identifier
  - `description`: String, task description (max 250 characters)
  - `completed`: Boolean, completion status (default False)
  - `created_at`: DateTime, timestamp of creation

### TaskList Object
- **Attributes**:
  - `tasks`: List of Task objects
  - `next_id`: Integer, counter for generating unique IDs

- **Methods**:
  - `add_task(description: str) -> int`
  - `get_task(task_id: int) -> Optional[Task]`
  - `get_all_tasks() -> List[Task]`
  - `update_task(task_id: int, new_description: str) -> bool`
  - `mark_complete(task_id: int) -> bool`
  - `mark_incomplete(task_id: int) -> bool`
  - `delete_task(task_id: int) -> bool`
  - `get_completed_tasks() -> List[Task]`
  - `get_pending_tasks() -> List[Task]`