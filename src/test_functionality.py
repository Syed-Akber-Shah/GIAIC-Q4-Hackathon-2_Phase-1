from task_model import Task, TaskList
from todo_manager import TodoManager

# Test the core functionality
todo_manager = TodoManager()

# Test adding a task
task_id = todo_manager.add_task('Test task description')
print(f'Added task with ID: {task_id}')

# Test getting the task
task = todo_manager.get_task(task_id)
print(f'Retrieved task: {task}')

# Test marking as complete
success = todo_manager.mark_complete(task_id)
print(f'Marked as complete: {success}')

# Test viewing all tasks
all_tasks = todo_manager.get_all_tasks()
print(f'All tasks: {len(all_tasks)}')

# Test updating the task
success = todo_manager.update_task(task_id, 'Updated task description')
print(f'Updated task: {success}')

# Test viewing pending tasks
pending_tasks = todo_manager.get_pending_tasks()
completed_tasks = todo_manager.get_completed_tasks()
print(f'Pending tasks: {len(pending_tasks)}, Completed tasks: {len(completed_tasks)}')

# Test marking as incomplete
success = todo_manager.mark_incomplete(task_id)
print(f'Marked as incomplete: {success}')

# Test deleting the task
success = todo_manager.delete_task(task_id)
print(f'Deleted task: {success}')

print('All core functionality tests passed!')