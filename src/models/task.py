"""
Task Model
Represents a todo item with id, title, description, status, and created_at fields
"""
from datetime import datetime
from typing import Optional


class Task:
    """Represents a todo item with id, title, description, status, and created_at fields"""

    def __init__(self, task_id: int, title: str, description: Optional[str] = None,
                 status: str = "Pending", created_at: Optional[datetime] = None):
        """
        Initialize a Task instance

        Args:
            task_id: Unique identifier for the task (auto-incremented)
            title: Task title (required, cannot be empty)
            description: Optional task description
            status: Task status, either "Pending" or "Completed" (default: "Pending")
            created_at: Timestamp of when the task was created (default: current time)
        """
        self.id = task_id
        self.title = title
        self.description = description if description is not None else ""
        self.status = status
        self.created_at = created_at if created_at is not None else datetime.now()

        # Validate the task on initialization
        self.validate()

    def validate(self) -> None:
        """
        Validate the task fields according to the specification

        Raises:
            ValueError: If validation fails
        """
        # Title must not be empty (after stripping whitespace)
        if not self.title or not self.title.strip():
            raise ValueError("Task title cannot be empty or whitespace-only")

        # Title must be a string with reasonable length limit (e.g., max 500 characters)
        if len(self.title) > 500:
            raise ValueError("Task title exceeds maximum length of 500 characters")

        # Status must be one of the allowed values: "Pending", "Completed"
        if self.status not in ["Pending", "Completed"]:
            raise ValueError(f"Task status must be 'Pending' or 'Completed', got '{self.status}'")

        # ID must be a positive integer
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError(f"Task ID must be a positive integer, got '{self.id}'")

    def toggle_status(self) -> None:
        """Toggle the task status between 'Pending' and 'Completed'"""
        if self.status == "Pending":
            self.status = "Completed"
        else:
            self.status = "Pending"

    def to_dict(self) -> dict:
        """Convert the task to a dictionary representation"""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at.isoformat()
        }

    def __str__(self) -> str:
        """String representation of the task"""
        return f"Task(id={self.id}, title='{self.title}', status='{self.status}', created_at={self.created_at})"

    def __repr__(self) -> str:
        """Developer-friendly representation of the task"""
        return self.__str__()