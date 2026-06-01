METADATA = {
    "id": 2650,
    "name": "Design Cancellable Function",
    "slug": "design-cancellable-function",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "math"],
    "difficulty": "medium",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Design a class that simulates a function which can be cancelled, returning the sum of its arguments or zero if cancelled.",
}

class CancellableFunction:
    def __init__(self, fn: callable) -> None:
        """
        Initializes the CancellableFunction with a given function.

        Args:
            fn (callable): The function to be wrapped.
        """
        self.fn = fn
        self.is_cancelled = False

    def cancel(self) -> None:
        """
        Cancels the next function call.

        Returns:
            None
        """
        self.is_cancelled = True

    def __call__(self, *args: int) -> int:
        """
        Calls the wrapped function if not cancelled, otherwise returns 0.

        Args:
            *args (int): Variable length integer arguments.

        Returns:
            int: The result of the function call or 0 if cancelled.

        Examples:
            >>> func = CancellableFunction(lambda x, y: x + y)
            >>> func(1, 2)
            3
            >>> func.cancel()
            >>> func(1, 2)
            0
        """
        # Check if the cancellation flag was set by a previous call to cancel()
        if self.is_cancelled:
            # Reset the flag for the next potential call
            self.is_cancelled = False
            return 0
        
        # If not cancelled, execute the original function and return result
        return self.fn(*args)

def solve():
    """
    A dummy solve function to satisfy the requirement structure.
    In a real LeetCode environment, the class above is the solution.
    """
    pass
