# Task Contract

## Task Management API

### Create Task
- **Action**: Add a new task to the system
- **Input**: title (string, required), description (string, optional)
- **Output**: Task object with id, title, description, status, created_at
- **Preconditions**: Title must not be empty
- **Postconditions**: New task exists in the repository with "Pending" status

### View All Tasks
- **Action**: Retrieve all tasks in the system
- **Input**: None
- **Output**: List of Task objects
- **Preconditions**: None
- **Postconditions**: Returns all existing tasks

### Get Task by ID
- **Action**: Retrieve a specific task by its ID
- **Input**: task_id (integer)
- **Output**: Task object or error if not found
- **Preconditions**: Task with given ID must exist
- **Postconditions**: Returns the requested task or error message

### Update Task
- **Action**: Update the title and/or description of a task
- **Input**: task_id (integer), title (string, optional), description (string, optional)
- **Output**: Success/failure indicator
- **Preconditions**: Task with given ID must exist
- **Postconditions**: Task fields updated or error returned

### Delete Task
- **Action**: Remove a task from the system
- **Input**: task_id (integer)
- **Output**: Success/failure indicator
- **Preconditions**: Task with given ID must exist
- **Postconditions**: Task removed from repository or error returned

### Toggle Task Status
- **Action**: Toggle a task's status between Pending and Completed
- **Input**: task_id (integer)
- **Output**: Success/failure indicator
- **Preconditions**: Task with given ID must exist
- **Postconditions**: Task status toggled or error returned

## Error Handling Contracts

### Invalid Input
- When invalid input is provided, the system returns a user-friendly error message

### Task Not Found
- When a requested task does not exist, the system returns an appropriate error message

### Validation Errors
- When validation fails (e.g., empty title), the system returns a specific error message