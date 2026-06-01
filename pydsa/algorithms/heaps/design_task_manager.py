METADATA = {
    "id": 3408,
    "name": "Design Task Manager",
    "slug": "design-task-manager",
    "category": "Design",
    "aliases": [],
    "tags": ["heap", "hash_map", "design", "priority_queue"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Design a task manager that supports adding, editing, deleting, and retrieving the task with the highest priority.",
}

import heapq

class TaskManager:
    def __init__(self, tasks: list[list[int]]):
        """
        Initializes the TaskManager with a list of tasks.
        Each task is [userId, taskId, priority].
        """
        # task_map stores taskId -> (userId, priority) for O(1) lookup and validation
        self.task_map: dict[int, tuple[int, int]] = {}
        # max_heap stores (-priority, -taskId, userId) to simulate max-heap behavior
        # We use negative values because Python's heapq is a min-heap
        self.max_heap: list[tuple[int, int, int]] = []
        
        for user_id, task_id, priority in tasks:
            self.add(user_id, task_id, priority)

    def add(self, user_id: int, task_id: int, priority: int) -> None:
        """
        Adds a new task or updates an existing task.
        """
        self.task_map[task_id] = (user_id, priority)
        # Push to heap. We include taskId in the tuple to handle tie-breaking 
        # and to ensure we can identify the specific task version.
        heapq.heappush(self.max_heap, (-priority, -task_id, user_id))

    def edit(self, task_id: int, new_priority: int) -> None:
        """
        Updates the priority of an existing task.
        """
        if task_id in self.task_map:
            user_id, _ = self.task_map[task_id]
            self.add(user_id, task_id, new_priority)

    def rmv(self, task_id: int) -> None:
        """
        Removes a task from the manager.
        """
        if task_id in self.task_map:
            del self.task_map[task_id]

    def execTop(self) -> int:
        """
        Executes the task with the highest priority. 
        If priorities are equal, the task with the highest taskId is chosen.
        Returns the userId of the executed task, or -1 if no tasks exist.
        """
        while self.max_heap:
            neg_priority, neg_task_id, user_id = self.max_heap[0]
            priority = -neg_priority
            task_id = -neg_task_id
            
            # Lazy deletion: Check if the task in the heap is still valid 
            # (i.e., it exists in task_map and has the same priority)
            if task_id in self.task_map and self.task_map[task_id] == (user_id, priority):
                # Task is valid, remove it and return user_id
                heapq.heappop(self.max_heap)
                del self.task_map[task_id]
                return user_id
            else:
                # Task was edited or removed, discard stale heap entry
                heapq.heappop(self.max_heap)
                
        return -1

def solve():
    """
    Example usage of the TaskManager class.
    """
    # Initial tasks: [[user1, task1, priority1], ...]
    tm = TaskManager([[1, 1, 10], [2, 2, 20]])
    tm.add(3, 3, 30)
    print(tm.execTop())  # Expected: 3 (task 3 has priority 30)
    tm.edit(1, 40)
    print(tm.execTop())  # Expected: 1 (task 1 now has priority 40)
    tm.rmv(2)
    print(tm.execTop())  # Expected: -1 (no tasks left)
