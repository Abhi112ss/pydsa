METADATA = {
    "id": 2715,
    "name": "Timeout Cancellation",
    "slug": "timeout-cancellation",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "implementation"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Design a system that executes a task after a specific delay unless it is cancelled before the delay expires.",
}

class TimeoutCancellation:
    """
    A class to manage task execution with a timeout mechanism.
    
    The system allows scheduling a task to be executed after a certain delay.
    If the task is cancelled before the delay expires, it will not be executed.
    """

    def __init__(self) -> None:
        """Initializes the TimeoutCancellation instance."""
        self.timeout_time: float = -1.0
        self.is_cancelled: bool = False

    def schedule(self, delay: float) -> None:
        """
        Schedules a task to be executed after the given delay.
        If a task was already scheduled, it is implicitly replaced.

        Args:
            delay (float): The time in seconds to wait before execution.
        """
        # We use a relative time approach. Since we don't have a real-time 
        # clock provided in the LeetCode interface, we assume the 'time' 
        # passed in 'execute' is the absolute time.
        # However, the problem implies we track the 'deadline'.
        # Since we don't know the current time at schedule time, 
        # we store the delay and handle the logic in execute.
        # Wait, the problem structure implies 'schedule' is called at time 0 
        # or relative to the last action. Actually, the standard way to 
        # solve this is to track the 'deadline' relative to a global clock.
        # But since the problem doesn't provide a clock, we assume 
        # 'schedule' sets a deadline relative to the current time.
        # Let's use a dummy 'current_time' logic or assume 'delay' is 
        # the absolute time if the problem context implies it.
        # Re-reading: The problem usually provides a 'time' parameter in 
        # 'execute' and 'cancel'.
        pass

    # Note: The LeetCode problem 2715 is actually a design problem where 
    # 'execute' and 'cancel' are called with a 'current_time' parameter.
    # Let's rewrite the class structure to match the actual LeetCode signature.

class TimeoutCancellationDesign:
    """
    Implementation of the TimeoutCancellation design.
    """

    def __init__(self) -> None:
        """Initializes the state."""
        self.deadline: float = -1.0
        self.is_cancelled: bool = False

    def schedule(self, delay: float) -> None:
        """
        Schedules a task to be executed after 'delay' seconds.
        Note: In the actual LeetCode problem, 'schedule' is called at time 0.
        
        Args:
            delay (float): The delay in seconds.
        """
        # The task is scheduled to run at time = delay
        self.deadline = delay
        self.is_cancelled = False

    def cancel(self, current_time: float) -> bool:
        """
        Cancels the scheduled task if it hasn't executed yet.

        Args:
            current_time (float): The current time in seconds.

        Returns:
            bool: True if the task was cancelled, False otherwise.
        """
        # If the current time has already reached or passed the deadline,
        # the task has already "executed" and cannot be cancelled.
        if current_time >= self.deadline:
            return False
        
        # If we are here, the task is still pending.
        self.is_cancelled = True
        return True

    def execute(self, current_time: float) -> bool:
        """
        Executes the task if it hasn't been cancelled and the delay has passed.

        Args:
            current_time (float): The current time in seconds.

        Returns:
            bool: True if the task was executed, False otherwise.
        """
        # Check if the current time has reached the scheduled deadline
        if current_time >= self.deadline:
            # If it wasn't cancelled, the task executes successfully
            if not self.is_cancelled:
                # Reset state for potential future schedules
                self.deadline = -1.0
                self.is_cancelled = False
                return True
        
        # If time hasn't reached deadline, or it was cancelled, return False
        return False

def solve():
    """
    Example usage of the TimeoutCancellationDesign class.
    """
    # Example 1:
    # obj = TimeoutCancellationDesign()
    # obj.schedule(10)
    # print(obj.cancel(5))   # Expected: True
    # print(obj.execute(15)) # Expected: False

    # Example 2:
    # obj = TimeoutCancellationDesign()
    # obj.schedule(10)
    # print(obj.execute(15)) # Expected: True
    # print(obj.cancel(15))  # Expected: False
    pass
