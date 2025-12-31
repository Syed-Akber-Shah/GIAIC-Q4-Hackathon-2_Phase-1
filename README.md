# In-Memory Command-Line Todo Application

A basic in-memory command-line todo application built with Python, designed as a hackathon-ready MVP demonstrating spec-driven development practices.

## Overview

This application implements the 5 core features of a todo application:
- Add tasks
- View all tasks
- Mark tasks as complete/incomplete
- Update task descriptions
- Delete tasks

All data is stored in-memory only, meaning tasks will be lost when the application exits.

## Setup Instructions

1. Ensure you have Python 3.13+ installed on your system
2. Clone this repository
3. Navigate to the project directory
4. Run the application from the src directory:

```bash
cd src
python main.py
```

## Features

- Menu-driven console interface
- Task management with unique IDs
- Status tracking (complete/incomplete)
- Input validation and error handling
- Clean, user-friendly prompts

## Usage

The application presents a menu with the following options:
1. Add Task - Create a new task with a description
2. View All Tasks - Display all tasks with their status
3. Mark Task Complete/Incomplete - Toggle the completion status of a task
4. Update Task - Modify the description of an existing task
5. Delete Task - Remove a task from the list
6. Exit - Quit the application

## Technical Details

- Language: Python 3.13+
- Storage: In-memory using Python lists and dictionaries
- Dependencies: Standard library only
- Architecture: MVC-style separation with models, services, and UI

## Project Structure

```
src/
├── main.py              # Console application entry point and menu loop
├── task_model.py        # Task data model and TaskList collection
└── todo_manager.py      # Business logic for todo operations
```

## Constraints

- Maximum of 1000 tasks supported
- Single-user application
- In-memory storage only (no persistence)
- Console-based interface only