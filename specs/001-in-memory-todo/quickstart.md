# Quickstart Guide: In-Memory Command-Line Todo Application

## Overview
This guide provides instructions for setting up and running the in-memory command-line todo application. The application implements the 5 core features: Add, Delete, Update, View, and Mark Complete.

## Prerequisites
- Python 3.13 or higher
- UV package manager

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install UV (if not already installed)
```bash
pip install uv
```

### 3. Create Virtual Environment and Install Dependencies
```bash
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

Note: Since this application uses only the Python standard library, no additional dependencies need to be installed.

### 4. Run the Application
```bash
cd src
python main.py
```

## Running the Application

### Starting the Application
1. Navigate to the `src` directory
2. Run `python main.py`
3. The main menu will appear with options for the 5 core features

### Main Menu Options
1. **Add Task**: Creates a new task with a description
2. **View Tasks**: Displays all tasks with their status
3. **Update Task**: Modifies the description of an existing task
4. **Mark Complete/Incomplete**: Toggles the completion status of a task
5. **Delete Task**: Removes a task from the list
6. **Exit**: Quits the application

### Using the Application
- Follow the on-screen prompts for each operation
- Enter task IDs when prompted (displayed in the task list)
- Enter task descriptions when prompted
- Use the main menu to navigate between operations

## Example Usage

### Adding a Task
1. Select "Add Task" from the main menu
2. Enter the task description when prompted
3. The task will be added with a unique ID and "incomplete" status

### Viewing Tasks
1. Select "View Tasks" from the main menu
2. All tasks will be displayed with their ID, description, and status
3. Tasks marked with [X] are complete; tasks marked with [ ] are incomplete

### Updating a Task
1. Select "Update Task" from the main menu
2. Enter the ID of the task you want to update
3. Enter the new description for the task

### Marking a Task Complete/Incomplete
1. Select "Mark Complete/Incomplete" from the main menu
2. Enter the ID of the task you want to update
3. The task's status will toggle between complete and incomplete

### Deleting a Task
1. Select "Delete Task" from the main menu
2. Enter the ID of the task you want to delete
3. Confirm the deletion when prompted

## Error Handling
- Invalid task IDs will result in an error message
- Empty task descriptions are not allowed
- The application will not crash on invalid input; instead, it will prompt for valid input

## Development
To modify the application:
- `main.py`: Contains the main menu and user interface logic
- `task_model.py`: Contains the Task and TaskList data models
- `todo_manager.py`: Contains the business logic for todo operations

## Limitations
- Data is stored only in memory and will be lost when the application exits
- Maximum of 1000 tasks supported
- Single-user application with no concurrent access
- No persistent storage or file export capabilities