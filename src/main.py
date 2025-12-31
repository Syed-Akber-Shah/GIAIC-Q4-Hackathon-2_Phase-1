"""
Console application entry point and menu loop for the in-memory todo application.

This module provides the main user interface for the todo application,
allowing users to interact with their tasks through a menu-driven console interface.
"""
from typing import Optional
import todo_manager
from todo_manager import TodoManager


def display_menu():
    """
    Display the main menu options to the user.
    """
    print("\n" + "="*40)
    print("TODO APPLICATION - MAIN MENU")
    print("="*40)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Mark Task Complete/Incomplete")
    print("4. Update Task")
    print("5. Delete Task")
    print("6. Exit")
    print("-"*40)


def get_user_choice() -> str:
    """
    Get and validate the user's menu choice.

    Returns:
        str: The user's menu choice (1-6)
    """
    while True:
        try:
            choice = input("Enter your choice (1-6): ").strip()
            if choice in ['1', '2', '3', '4', '5', '6']:
                return choice
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except KeyboardInterrupt:
            print("\n\nExiting application...")
            return '6'  # Return exit option if user interrupts


def add_task_interface(todo_manager_instance: TodoManager):
    """
    Handle the user interface for adding a new task.

    Args:
        todo_manager_instance (TodoManager): The TodoManager instance to use
    """
    print("\n--- ADD TASK ---")
    description = input("Enter task description: ").strip()

    if not description:
        print("Error: Task description cannot be empty.")
        return

    if len(description) > 250:
        print("Error: Task description cannot exceed 250 characters.")
        return

    try:
        task_id = todo_manager_instance.add_task(description)
        print(f"Task added successfully with ID: {task_id}")
    except ValueError as e:
        print(f"Error: {e}")


def view_tasks_interface(todo_manager_instance: TodoManager):
    """
    Handle the user interface for viewing tasks.

    Args:
        todo_manager_instance (TodoManager): The TodoManager instance to use
    """
    print("\n--- VIEW TASKS ---")
    tasks = todo_manager_instance.get_all_tasks()

    if not tasks:
        print("No tasks found.")
        return

    print("All Tasks:")
    for task in tasks:
        print(f"  {task}")


def mark_task_interface(todo_manager_instance: TodoManager):
    """
    Handle the user interface for marking a task complete/incomplete.

    Args:
        todo_manager_instance (TodoManager): The TodoManager instance to use
    """
    print("\n--- MARK TASK COMPLETE/INCOMPLETE ---")

    if not get_and_validate_task_id(todo_manager_instance, "mark"):
        return

    task_id = int(input("Enter task ID: "))
    task = todo_manager_instance.get_task(task_id)

    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    if task.completed:
        success = todo_manager_instance.mark_incomplete(task_id)
        if success:
            print(f"Task {task_id} marked as incomplete.")
    else:
        success = todo_manager_instance.mark_complete(task_id)
        if success:
            print(f"Task {task_id} marked as complete.")


def update_task_interface(todo_manager_instance: TodoManager):
    """
    Handle the user interface for updating a task.

    Args:
        todo_manager_instance (TodoManager): The TodoManager instance to use
    """
    print("\n--- UPDATE TASK ---")

    if not get_and_validate_task_id(todo_manager_instance, "update"):
        return

    task_id = int(input("Enter task ID: "))
    task = todo_manager_instance.get_task(task_id)

    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    new_description = input(f"Enter new description (current: '{task.description}'): ").strip()

    if not new_description:
        print("Error: Task description cannot be empty.")
        return

    if len(new_description) > 250:
        print("Error: Task description cannot exceed 250 characters.")
        return

    try:
        success = todo_manager_instance.update_task(task_id, new_description)
        if success:
            print(f"Task {task_id} updated successfully.")
        else:
            print(f"Failed to update task {task_id}.")
    except ValueError as e:
        print(f"Error: {e}")


def delete_task_interface(todo_manager_instance: TodoManager):
    """
    Handle the user interface for deleting a task.

    Args:
        todo_manager_instance (TodoManager): The TodoManager instance to use
    """
    print("\n--- DELETE TASK ---")

    if not get_and_validate_task_id(todo_manager_instance, "delete"):
        return

    task_id = int(input("Enter task ID: "))
    task = todo_manager_instance.get_task(task_id)

    if not task:
        print(f"Error: Task with ID {task_id} not found.")
        return

    confirm = input(f"Are you sure you want to delete task '{task.description}'? (y/N): ").strip().lower()

    if confirm in ['y', 'yes']:
        success = todo_manager_instance.delete_task(task_id)
        if success:
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Failed to delete task {task_id}.")
    else:
        print("Deletion cancelled.")


def get_and_validate_task_id(todo_manager_instance: TodoManager, operation: str) -> bool:
    """
    Helper function to get and validate a task ID from the user.

    Args:
        todo_manager_instance (TodoManager): The TodoManager instance to use
        operation (str): The operation being performed (for error messages)

    Returns:
        bool: True if a valid task ID was entered, False otherwise
    """
    # First, check if there are any tasks
    tasks = todo_manager_instance.get_all_tasks()
    if not tasks:
        print(f"No tasks available to {operation}. Please add a task first.")
        return False

    while True:
        try:
            task_id_input = input("Enter task ID: ").strip()
            if not task_id_input:
                print("Task ID cannot be empty.")
                continue

            task_id = int(task_id_input)
            if task_id <= 0:
                print("Task ID must be a positive integer.")
                continue

            return True
        except ValueError:
            print("Task ID must be a valid integer.")


def main():
    """
    Main function to run the todo application.
    """
    print("Welcome to the In-Memory Command-Line Todo Application!")

    todo_manager_instance = TodoManager()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == '1':
            add_task_interface(todo_manager_instance)
        elif choice == '2':
            view_tasks_interface(todo_manager_instance)
        elif choice == '3':
            mark_task_interface(todo_manager_instance)
        elif choice == '4':
            update_task_interface(todo_manager_instance)
        elif choice == '5':
            delete_task_interface(todo_manager_instance)
        elif choice == '6':
            print("\nThank you for using the Todo Application. Goodbye!")
            break


if __name__ == "__main__":
    main()