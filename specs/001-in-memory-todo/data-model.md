# Data Model: In-Memory Command-Line Todo Application

## Overview
This document defines the data structures and relationships for the in-memory command-line todo application. The model supports the 5 core features: Add, Delete, Update, View, and Mark Complete.

## Core Entities

### Task
The Task entity represents a single todo item with the following attributes:

- **id**: `int` - Unique identifier for the task (auto-generated)
- **description**: `str` - Text content describing the task (max 250 characters)
- **completed**: `bool` - Status indicator (True for complete, False for incomplete)
- **created_at**: `datetime` - Timestamp when the task was created

#### Validation Rules
- `id` must be unique within the TaskList
- `description` must not be empty or None
- `description` must not exceed 250 characters
- `completed` defaults to False when creating a new task

#### State Transitions
- A Task can transition from incomplete (completed=False) to complete (completed=True)
- A Task can transition from complete (completed=True) back to incomplete (completed=False)

### TaskList
The TaskList entity represents a collection of Task objects with the following attributes:

- **tasks**: `List[Task]` - Collection of Task objects
- **next_id**: `int` - Counter for generating unique IDs (starts at 1)

#### Operations
- `add_task(description: str) -> int`: Adds a new task and returns its ID
- `get_task(task_id: int) -> Optional[Task]`: Retrieves a task by ID
- `get_all_tasks() -> List[Task]`: Returns all tasks
- `update_task(task_id: int, new_description: str) -> bool`: Updates task description
- `mark_complete(task_id: int) -> bool`: Marks a task as complete
- `mark_incomplete(task_id: int) -> bool`: Marks a task as incomplete
- `delete_task(task_id: int) -> bool`: Removes a task from the list
- `get_completed_tasks() -> List[Task]`: Returns only completed tasks
- `get_pending_tasks() -> List[Task]`: Returns only pending tasks

#### Validation Rules
- Task IDs must be unique within the collection
- Task IDs must be positive integers
- No duplicate tasks allowed
- Maximum of 1000 tasks allowed in the collection

## Relationships

### TaskList to Task
- One TaskList contains many Tasks (1 to many relationship)
- Tasks exist only within the context of a TaskList
- When a TaskList is cleared, all its Tasks are removed

## Data Lifecycle

### Creation
1. A TaskList is initialized with an empty list and next_id=1
2. When a new Task is added:
   - The description is validated
   - A unique ID is assigned (using next_id counter)
   - The completed status is set to False
   - The created_at timestamp is set to current time
   - The Task is added to the TaskList

### Retrieval
1. Tasks can be retrieved individually by ID
2. Tasks can be retrieved in groups (all, completed, pending)
3. The TaskList maintains the order of insertion

### Update
1. A Task's description can be updated by providing its ID
2. A Task's completion status can be toggled by providing its ID

### Deletion
1. A Task can be removed from the TaskList by providing its ID
2. The TaskList maintains its integrity after deletion

## Implementation Details

### Memory Management
- All data is stored in Python lists and dictionaries
- No external storage is used
- Data is lost when the application terminates

### Concurrency Considerations
- Single-user application with no concurrent access
- No locking mechanisms required
- Operations are synchronous

### Error Handling
- Invalid task IDs return None or False depending on the operation
- Invalid descriptions raise appropriate exceptions
- Boundary conditions (empty list, etc.) are handled gracefully