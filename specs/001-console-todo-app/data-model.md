# Data Model: Console Todo App

## Task Entity

### Fields
- **id**: Integer (auto-incremented, required)
  - Auto-generated unique identifier for each task
  - Starts at 1 and increments for each new task
- **title**: String (required)
  - Task title with minimum length validation
  - Cannot be empty or whitespace-only
- **description**: String (optional, nullable)
  - Optional task description
  - Can be empty/None
- **status**: String (required, enum)
  - Values: "Pending" | "Completed"
  - Default: "Pending" for new tasks
- **created_at**: DateTime (required)
  - Timestamp of when the task was created
  - Format: ISO 8601 string representation

### Validation Rules
- Title must not be empty (after stripping whitespace)
- Title must be a string with reasonable length limit (e.g., max 500 characters)
- Status must be one of the allowed values: "Pending", "Completed"
- ID must be a positive integer

### State Transitions
- New Task: status = "Pending" (default)
- Toggle Status: "Pending" ↔ "Completed" (toggle operation)

### Relationships
- None (standalone entity)

## Task Repository Interface

### Methods
- **create_task(title: str, description: str = None) -> Task**
  - Creates a new task with auto-generated ID
  - Sets status to "Pending" by default
  - Sets creation timestamp
- **get_all_tasks() -> List[Task]**
  - Returns all tasks in the repository
- **get_task_by_id(task_id: int) -> Task | None**
  - Returns task with given ID or None if not found
- **update_task(task_id: int, title: str = None, description: str = None) -> bool**
  - Updates task fields if task exists
  - Returns True if successful, False if task not found
- **delete_task(task_id: int) -> bool**
  - Removes task from repository
  - Returns True if successful, False if task not found
- **toggle_task_status(task_id: int) -> bool**
  - Toggles task status between "Pending" and "Completed"
  - Returns True if successful, False if task not found