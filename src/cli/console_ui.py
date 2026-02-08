"""
Console UI
Menu-driven console interface for the todo application
"""
from ..services.task_repository import TaskRepository
from ..models.task import Task
from typing import Optional
import sys


class ConsoleUI:
    """Console user interface for the todo application"""

    def __init__(self, task_repository: TaskRepository):
        """
        Initialize the console UI with a task repository

        Args:
            task_repository: The task repository to use for operations
        """
        self.task_repo = task_repository

    def run(self):
        """Main application loop"""
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ").strip()

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.mark_task_completion()
            elif choice == "6":
                print("Exiting the application. Goodbye!")
                break  # Changed from sys.exit(0) to break for graceful exit
            else:
                print(f"Invalid choice: '{choice}'. Please enter a number between 1-6.")
                input("Press Enter to continue...")

    def display_menu(self):
        """Display the main menu options"""
        print("\n" + "="*40)
        print("CONSOLE TODO APPLICATION")
        print("="*40)
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Mark Task Complete / Incomplete")
        print("6. Exit")
        print("="*40)

    def add_task(self):
        """Add a new task to the repository"""
        print("\n--- Add New Task ---")
        title = input("Enter task title: ").strip()

        if not title:
            print("Error: Task title cannot be empty.")
            input("Press Enter to continue...")
            return

        description = input("Enter task description (optional, press Enter to skip): ").strip()
        if not description:
            description = None

        try:
            task = self.task_repo.create_task(title=title, description=description)
            print(f"Task '{task.title}' added successfully with ID {task.id}")
        except ValueError as e:
            print(f"Error creating task: {e}")

        input("Press Enter to continue...")

    def view_tasks(self):
        """Display all tasks in the repository"""
        print("\n--- View All Tasks ---")
        tasks = self.task_repo.get_all_tasks()

        if not tasks:
            print("No tasks found.")
        else:
            print(f"{'ID':<4} {'Title':<20} {'Status':<12} {'Created At':<20}")
            print("-" * 60)
            for task in tasks:
                from ..lib.timestamp_utils import format_timestamp
                created_str = format_timestamp(task.created_at, "%Y-%m-%d %H:%M")
                print(f"{task.id:<4} {task.title[:19]:<20} {task.status:<12} {created_str:<20}")

        input("\nPress Enter to continue...")

    def update_task(self):
        """Update an existing task"""
        print("\n--- Update Task ---")
        task_id_str = input("Enter task ID to update: ").strip()

        # Validate task ID input
        if not task_id_str.isdigit():
            print(f"Error: '{task_id_str}' is not a valid task ID. Please enter a number.")
            input("Press Enter to continue...")
            return

        task_id = int(task_id_str)

        # Check if task exists
        existing_task = self.task_repo.get_task_by_id(task_id)
        if not existing_task:
            print(f"Error: Task with ID {task_id} not found.")
            input("Press Enter to continue...")
            return

        print(f"Current task: {existing_task.title} (Status: {existing_task.status})")

        # Get new title or keep existing
        new_title_input = input(f"Enter new title (current: '{existing_task.title}', press Enter to keep): ").strip()
        new_title = new_title_input if new_title_input else existing_task.title

        # Get new description or keep existing
        new_description_input = input(f"Enter new description (current: '{existing_task.description}', press Enter to keep): ").strip()
        new_description = new_description_input if new_description_input != "" else existing_task.description

        try:
            success = self.task_repo.update_task(task_id=task_id, title=new_title, description=new_description)
            if success:
                print(f"Task with ID {task_id} updated successfully.")
            else:
                print(f"Failed to update task with ID {task_id}.")
        except ValueError as e:
            print(f"Error updating task: {e}")

        input("Press Enter to continue...")

    def delete_task(self):
        """Delete a task from the repository"""
        print("\n--- Delete Task ---")
        task_id_str = input("Enter task ID to delete: ").strip()

        # Validate task ID input
        if not task_id_str.isdigit():
            print(f"Error: '{task_id_str}' is not a valid task ID. Please enter a number.")
            input("Press Enter to continue...")
            return

        task_id = int(task_id_str)

        # Check if task exists before deletion
        existing_task = self.task_repo.get_task_by_id(task_id)
        if not existing_task:
            print(f"Error: Task with ID {task_id} not found.")
            input("Press Enter to continue...")
            return

        print(f"About to delete task: {existing_task.title}")
        confirm = input("Are you sure you want to delete this task? (y/N): ").strip().lower()

        if confirm in ['y', 'yes']:
            success = self.task_repo.delete_task(task_id)
            if success:
                print(f"Task with ID {task_id} deleted successfully.")
            else:
                print(f"Failed to delete task with ID {task_id}.")
        else:
            print("Task deletion cancelled.")

        input("Press Enter to continue...")

    def mark_task_completion(self):
        """Toggle a task's completion status"""
        print("\n--- Mark Task Complete / Incomplete ---")
        task_id_str = input("Enter task ID to toggle status: ").strip()

        # Validate task ID input
        if not task_id_str.isdigit():
            print(f"Error: '{task_id_str}' is not a valid task ID. Please enter a number.")
            input("Press Enter to continue...")
            return

        task_id = int(task_id_str)

        # Check if task exists
        existing_task = self.task_repo.get_task_by_id(task_id)
        if not existing_task:
            print(f"Error: Task with ID {task_id} not found.")
            input("Press Enter to continue...")
            return

        print(f"Current status for '{existing_task.title}': {existing_task.status}")

        success = self.task_repo.toggle_task_status(task_id)
        if success:
            updated_task = self.task_repo.get_task_by_id(task_id)
            print(f"Task status updated to: {updated_task.status}")
        else:
            print(f"Failed to update task status for ID {task_id}.")

        input("Press Enter to continue...")