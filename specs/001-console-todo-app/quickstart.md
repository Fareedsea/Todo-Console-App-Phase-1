# Quickstart: Console Todo App

## Running the Application

1. Ensure Python 3.13+ is installed on your system
2. Navigate to the project root directory
3. Run the application:
   ```bash
   python src/lib/main.py
   ```

## Using the Application

1. The application will display a menu with the following options:
   - 1. Add Task
   - 2. View Tasks
   - 3. Update Task
   - 4. Delete Task
   - 5. Mark Task Complete / Incomplete
   - 6. Exit

2. Enter the number corresponding to your desired action and follow the prompts.

## Example Usage

### Adding a Task
1. Select option 1 (Add Task)
2. Enter the task title when prompted
3. Optionally enter a task description
4. The task will be created with a unique ID and "Pending" status

### Viewing Tasks
1. Select option 2 (View Tasks)
2. All tasks will be displayed with their ID, title, status, and creation time

### Updating a Task
1. Select option 3 (Update Task)
2. Enter the task ID you want to update
3. Enter the new title and/or description when prompted

### Deleting a Task
1. Select option 4 (Delete Task)
2. Enter the task ID you want to delete
3. The task will be removed from the system

### Marking Task Complete/Incomplete
1. Select option 5 (Mark Task Complete / Incomplete)
2. Enter the task ID you want to toggle
3. The task status will toggle between "Pending" and "Completed"