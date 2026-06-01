METADATA = {
    "id": 2590,
    "name": "Design a Todo List",
    "slug": "design-a-todo-list",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "list"],
    "difficulty": "medium",
    "time_complexity": "O(1) for most operations, O(n) for remove",
    "space_complexity": "O(n)",
    "description": "Design a data structure that supports adding, removing, updating, and retrieving tasks by index.",
}

class TodoList:
    """
    A class representing a Todo List that supports basic CRUD operations.
    """

    def __init__(self, tasks: list[list[str]]):
        """
        Initializes the TodoList with a list of tasks.

        Args:
            tasks (list[list[str]]): A list where each element is a list containing 
                                     [userId, taskId, priority, description].
        """
        # We store tasks in a list for O(1) access by index.
        # Each task is represented as a dictionary for better readability and maintenance.
        self.tasks: list[dict] = []
        for task in tasks:
            self.tasks.append({
                "userId": task[0],
                "taskId": task[1],
                "priority": task[2],
                "description": task[3]
            })

    def add(self, userId: int, taskId: int, priority: int, description: str) -> None:
        """
        Adds a new task to the end of the list.

        Args:
            userId (int): The ID of the user.
            taskId (int): The ID of the task.
            priority (int): The priority of the task.
            description (str): The description of the task.
        """
        self.tasks.append({
            "userId": userId,
            "taskId": taskId,
            "priority": priority,
            "description": description
        })

    def edit(self, index: int, newDescription: str) -> None:
        """
        Updates the description of a task at a specific index.

        Args:
            index (int): The index of the task to edit.
            newDescription (str): The new description for the task.
        """
        # Direct index access allows O(1) update.
        self.tasks[index]["description"] = newDescription

    def complete(self, index: int) -> None:
        """
        Removes a task from the list by its index.

        Args:
            index (int): The index of the task to complete.
        """
        # Removing an element from a list is O(n) in the worst case.
        self.tasks.pop(index)

    def show(self, index: int) -> str | None:
        """
        Returns the task details at a specific index as a formatted string.

        Args:
            index (int): The index of the task to retrieve.

        Returns:
            str | None: A formatted string "[userId,taskId,priority,description]" 
                        or None if index is invalid.
        """
        if 0 <= index < len(self.tasks):
            task = self.tasks[index]
            return f"[{task['userId']},{task['taskId']},{task['priority']},{task['description']}]"
        return None

def solve():
    """
    Example usage of the TodoList class.
    """
    initial_tasks = [[0, 0, 1, "task0"], [1, 1, 3, "task1"]]
    todo = TodoList(initial_tasks)
    
    todo.add(2, 2, 2, "task2")
    print(todo.show(2))  # Expected: "[2,2,2,task2]"
    
    todo.edit(0, "new_task0")
    print(todo.show(0))  # Expected: "[0,0,1,new_task0]"
    
    todo.complete(1)
    print(todo.show(1))  # Expected: "[2,2,2,task2]" (index 1 was task1, now task2 is at index 1)
