"""
Task Repository
In-memory task storage and operations
"""
from typing import List, Optional, Dict, Any
from ..models.task import Task


class TaskRepository:
    """Task repository for in-memory task storage and operations"""

    def __init__(self):
        """Initialize the task repository with empty storage and ID counter"""
        self._tasks: Dict[int, Task] = {}
        self._next_id = 1

    def create_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Create a new task with auto-generated ID

        Args:
            title: Task title (required)
            description: Optional task description

        Returns:
            Task: The created task with auto-generated ID and "Pending" status

        Raises:
            ValueError: If title validation fails
        """
        task_id = self._next_id
        self._next_id += 1

        # Create task with auto-generated ID, "Pending" status by default
        task = Task(task_id=task_id, title=title, description=description, status="Pending")
        self._tasks[task_id] = task

        return task

    def get_all_tasks(self) -> List[Task]:
        """
        Get all tasks in the repository

        Returns:
            List[Task]: All tasks in the repository
        """
        return list(self._tasks.values())

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a specific task by its ID

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            Task: The task with the given ID, or None if not found
        """
        return self._tasks.get(task_id)

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> bool:
        """
        Update task fields if task exists

        Args:
            task_id: The ID of the task to update
            title: New title (optional)
            description: New description (optional)

        Returns:
            bool: True if successful, False if task not found
        """
        if task_id not in self._tasks:
            return False

        task = self._tasks[task_id]

        # Use the existing values if not provided
        new_title = title if title is not None else task.title
        new_description = description if description is not None else task.description

        # Create a new task with updated values (to trigger validation)
        updated_task = Task(
            task_id=task_id,
            title=new_title,
            description=new_description,
            status=task.status,
            created_at=task.created_at
        )

        # Update the task in the repository
        self._tasks[task_id] = updated_task
        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Remove a task from the repository

        Args:
            task_id: The ID of the task to delete

        Returns:
            bool: True if successful, False if task not found
        """
        if task_id not in self._tasks:
            return False

        del self._tasks[task_id]
        return True

    def toggle_task_status(self, task_id: int) -> bool:
        """
        Toggle a task's status between "Pending" and "Completed"

        Args:
            task_id: The ID of the task to toggle

        Returns:
            bool: True if successful, False if task not found
        """
        if task_id not in self._tasks:
            return False

        task = self._tasks[task_id]
        task.toggle_status()
        return True

    def get_next_id(self) -> int:
        """
        Get the next available task ID (for testing purposes)

        Returns:
            int: The next available task ID
        """
        return self._next_id