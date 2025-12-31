"""
Task model for the in-memory command-line todo application.

This module defines the Task and TaskList classes that represent
the core data structures for the todo application.
"""
from datetime import datetime
from typing import List, Optional


class Task:
    """
    Represents a single todo item with attributes including ID, description, and status.
    """
    def __init__(self, task_id: int, description: str, completed: bool = False):
        """
        Initialize a Task instance.

        Args:
            task_id (int): Unique identifier for the task
            description (str): Task description (max 250 characters)
            completed (bool): Completion status (default False)
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")
        
        if len(description) > 250:
            raise ValueError("Task description cannot exceed 250 characters")
        
        self.id = task_id
        self.description = description.strip()
        self.completed = completed
        self.created_at = datetime.now()

    def __str__(self) -> str:
        """
        String representation of the task.
        
        Returns:
            str: Formatted string with task status, ID, and description
        """
        status = "[X]" if self.completed else "[ ]"
        return f"{status} {self.id}. {self.description}"


class TaskList:
    """
    Collection of Task entities managed in memory, supporting operations like 
    add, delete, update, view, and mark complete.
    """
    def __init__(self):
        """
        Initialize a TaskList instance with an empty list and ID counter.
        """
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, description: str) -> int:
        """
        Add a new task to the task list.

        Args:
            description (str): Description of the new task

        Returns:
            int: ID of the newly created task
        """
        if len(self.tasks) >= 1000:
            raise Exception("Maximum task limit (1000) reached")
        
        task_id = self.next_id
        task = Task(task_id, description)
        self.tasks.append(task)
        self.next_id += 1
        return task_id

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in the task list.

        Returns:
            List[Task]: List of all tasks
        """
        return self.tasks.copy()

    def get_completed_tasks(self) -> List[Task]:
        """
        Retrieve only completed tasks.

        Returns:
            List[Task]: List of completed tasks
        """
        return [task for task in self.tasks if task.completed]

    def get_pending_tasks(self) -> List[Task]:
        """
        Retrieve only pending (incomplete) tasks.

        Returns:
            List[Task]: List of pending tasks
        """
        return [task for task in self.tasks if not task.completed]

    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Update the description of an existing task.

        Args:
            task_id (int): ID of the task to update
            new_description (str): New description for the task

        Returns:
            bool: True if update was successful, False otherwise
        """
        task = self.get_task(task_id)
        if task:
            if not new_description or not new_description.strip():
                raise ValueError("Task description cannot be empty")
            
            if len(new_description) > 250:
                raise ValueError("Task description cannot exceed 250 characters")
            
            task.description = new_description.strip()
            return True
        return False

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id (int): ID of the task to mark complete

        Returns:
            bool: True if marking complete was successful, False otherwise
        """
        task = self.get_task(task_id)
        if task:
            task.completed = True
            return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id (int): ID of the task to mark incomplete

        Returns:
            bool: True if marking incomplete was successful, False otherwise
        """
        task = self.get_task(task_id)
        if task:
            task.completed = False
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the task list.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if deletion was successful, False otherwise
        """
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False