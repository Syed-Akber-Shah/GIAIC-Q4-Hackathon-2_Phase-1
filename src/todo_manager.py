"""
Business logic for todo operations in the in-memory command-line todo application.

This module defines the TodoManager class that handles all operations related to tasks,
including adding, viewing, updating, marking complete/incomplete, and deleting tasks.
"""
from typing import List, Optional
from task_model import Task, TaskList


class TodoManager:
    """
    Handles business logic for todo operations, managing a TaskList instance
    and providing methods for all required todo operations.
    """
    def __init__(self):
        """
        Initialize a TodoManager instance with a TaskList.
        """
        self.task_list = TaskList()

    def add_task(self, description: str) -> int:
        """
        Add a new task with the given description.

        Args:
            description (str): Description of the new task (max 250 characters)

        Returns:
            int: ID of the newly created task

        Raises:
            ValueError: If description is empty or exceeds 250 characters
        """
        return self.task_list.add_task(description)

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieve a task by its ID.

        Args:
            task_id (int): ID of the task to retrieve

        Returns:
            Optional[Task]: The task if found, None otherwise
        """
        return self.task_list.get_task(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Retrieve all tasks in the task list.

        Returns:
            List[Task]: List of all tasks
        """
        return self.task_list.get_all_tasks()

    def get_completed_tasks(self) -> List[Task]:
        """
        Retrieve only completed tasks.

        Returns:
            List[Task]: List of completed tasks
        """
        return self.task_list.get_completed_tasks()

    def get_pending_tasks(self) -> List[Task]:
        """
        Retrieve only pending (incomplete) tasks.

        Returns:
            List[Task]: List of pending tasks
        """
        return self.task_list.get_pending_tasks()

    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Update the description of an existing task.

        Args:
            task_id (int): ID of the task to update
            new_description (str): New description for the task

        Returns:
            bool: True if update was successful, False otherwise

        Raises:
            ValueError: If new description is empty or exceeds 250 characters
        """
        return self.task_list.update_task(task_id, new_description)

    def mark_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id (int): ID of the task to mark complete

        Returns:
            bool: True if marking complete was successful, False otherwise
        """
        return self.task_list.mark_complete(task_id)

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id (int): ID of the task to mark incomplete

        Returns:
            bool: True if marking incomplete was successful, False otherwise
        """
        return self.task_list.mark_incomplete(task_id)

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the task list.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if deletion was successful, False otherwise
        """
        return self.task_list.delete_task(task_id)