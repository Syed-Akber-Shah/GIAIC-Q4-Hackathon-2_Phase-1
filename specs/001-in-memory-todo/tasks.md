# Implementation Tasks: In-Memory Command-Line Todo Application

**Feature**: In-Memory Command-Line Todo Application  
**Branch**: `001-in-memory-todo`  
**Created**: 2026-01-01  
**Based on**: plan.md, spec.md, data-model.md, contracts/, research.md

## Implementation Strategy

MVP-first approach with incremental delivery. Each user story is implemented as a complete, independently testable increment. Start with foundational components, then implement user stories in priority order (P1, P2, P3...). Each story includes all necessary components (models, services, UI) to be fully functional.

## Phase 1: Setup

Initialize project structure and foundational components that all user stories depend on.

- [X] T001 Create project directory structure: src/, specs/, history/
- [X] T002 Initialize pyproject.toml with Python 3.13+ requirement
- [X] T003 Create src/ directory and all required module files (main.py, task_model.py, todo_manager.py)

## Phase 2: Foundational Components

Implement core components that all user stories depend on.

- [X] T004 [P] Create Task class in src/task_model.py with id, description, completed, created_at attributes
- [X] T005 [P] Create TaskList class in src/task_model.py with tasks list and next_id counter
- [X] T006 [P] Implement Task validation rules (description length, non-empty) in src/task_model.py
- [X] T007 [P] Create TodoManager class in src/todo_manager.py with task_list attribute
- [X] T008 [P] Implement basic menu loop in src/main.py with options placeholder

## Phase 3: User Story 1 - Add New Tasks (Priority: P1)

As a user, I want to add new tasks to my todo list so that I can keep track of what I need to do.

**Independent Test**: Can be fully tested by adding a task through the console interface and verifying it appears in the task list, delivering the core value of capturing tasks.

- [X] T009 [US1] Implement add_task method in TodoManager with description validation and ID generation
- [X] T010 [US1] Add menu option for adding tasks in main.py
- [X] T011 [US1] Implement user input handling for task description in main.py
- [X] T012 [US1] Display confirmation message after task is added with its ID
- [X] T013 [US1] Handle empty description error with appropriate message
- [X] T014 [US1] Validate description length (max 250 characters) with error message

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

As a user, I want to view all my tasks so that I can see what I need to do.

**Independent Test**: Can be fully tested by viewing the list of tasks, delivering the core value of task visibility.

- [X] T015 [US2] Implement get_all_tasks method in TodoManager
- [X] T016 [US2] Implement get_pending_tasks and get_completed_tasks methods in TodoManager
- [X] T017 [US2] Add menu option for viewing tasks in main.py
- [X] T018 [US2] Format and display tasks with ID, description, and status indicators [ ]/[X]
- [X] T019 [US2] Handle empty task list with appropriate message

## Phase 5: User Story 3 - Mark Tasks as Complete (Priority: P2)

As a user, I want to mark tasks as complete so that I can track my progress and know what I've already done.

**Independent Test**: Can be fully tested by marking a task as complete and verifying its status changes, delivering the value of progress tracking.

- [X] T020 [US3] Implement mark_complete and mark_incomplete methods in TodoManager
- [X] T021 [US3] Add menu option for marking tasks complete/incomplete in main.py
- [X] T022 [US3] Implement user input handling for task ID in main.py
- [X] T023 [US3] Validate task ID exists before attempting to mark complete
- [X] T024 [US3] Display confirmation message after status change

## Phase 6: User Story 4 - Update Task Description (Priority: P2)

As a user, I want to update the description of my tasks so that I can refine or correct them as needed.

**Independent Test**: Can be fully tested by updating a task description and verifying the change, delivering the value of task refinement.

- [X] T025 [US4] Implement update_task method in TodoManager with description validation
- [X] T026 [US4] Add menu option for updating tasks in main.py
- [X] T027 [US4] Implement user input handling for task ID and new description in main.py
- [X] T028 [US4] Validate task ID exists before attempting to update
- [X] T029 [US4] Validate new description length (max 250 characters) with error message
- [X] T030 [US4] Display confirmation message after task update

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

As a user, I want to delete tasks that are no longer needed so that I can keep my list clean and focused.

**Independent Test**: Can be fully tested by deleting a task and verifying it's removed from the list, delivering the value of list management.

- [X] T031 [US5] Implement delete_task method in TodoManager
- [X] T032 [US5] Add menu option for deleting tasks in main.py
- [X] T033 [US5] Implement user input handling for task ID in main.py
- [X] T034 [US5] Validate task ID exists before attempting to delete
- [X] T035 [US5] Display confirmation message after task deletion
- [X] T036 [US5] Handle attempt to delete non-existent task with error message

## Phase 8: Error Handling & Edge Cases

Implement comprehensive error handling for all operations.

- [X] T037 Implement validation for non-numeric IDs when numeric is expected
- [X] T038 Handle invalid menu selections with appropriate error messages
- [X] T039 Implement boundary condition handling for maximum task limit (1000 tasks)
- [X] T040 Add graceful handling for all edge cases identified in spec

## Phase 9: Polish & Cross-Cutting Concerns

Final improvements and integration.

- [X] T041 Enhance user prompts and messages for better UX
- [X] T042 Add comprehensive docstrings to all classes and methods
- [X] T043 Add type hints to all functions and methods
- [X] T044 Implement consistent formatting across all output
- [X] T045 Test complete workflow: Add → View → Update → Mark Complete → Delete → Exit
- [X] T046 Update README.md with project overview and setup instructions

## Dependencies

User stories are designed to be as independent as possible, but there are some dependencies:
- All user stories depend on Phase 1 (Setup) and Phase 2 (Foundational Components) being completed
- US2 (View Tasks) is helpful for testing other user stories but not strictly required
- US3 (Mark Complete) and US4 (Update Task) both require US1 (Add Task) to have tasks to work with for testing

## Parallel Execution Opportunities

- T004-T006 (Task model components) can be developed in parallel with T007 (TodoManager)
- T008 (Menu loop) can be developed in parallel with model components
- Each user story phase can be developed independently after foundational components are complete
- T041-T046 (Polish phase) can be done in parallel across multiple files

## MVP Scope

Minimal Viable Product includes:
- Phase 1: Setup
- Phase 2: Foundational Components
- Phase 3: User Story 1 (Add Tasks)
- Phase 4: User Story 2 (View Tasks)
- T037, T038 (Basic error handling)
- T041-T043, T045, T046 (Essential polish)