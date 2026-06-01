METADATA = {
    "id": 2676,
    "name": "Throttle",
    "slug": "throttle",
    "category": "Design",
    "aliases": [],
    "tags": ["design", "time"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(1)",
    "description": "Design a class that limits the execution of a function to once every specified interval.",
}


class Throttler:
    """
    A throttling utility that allows an operation to execute
    at most once every `limit` milliseconds.
    """

    def __init__(self, limit: int):
        """
        Initialize the throttler.

        Args:
            limit (int): Minimum interval (in milliseconds)
                between successful executions.
        """
        self.limit = limit
        self.last_execution_time = -1

    def allow(self, current_time: int) -> bool:
        """
        Check whether an operation is allowed to execute.

        Args:
            current_time (int): Current timestamp in milliseconds.

        Returns:
            bool:
                True if execution is allowed.
                False otherwise.

        Examples:
            >>> throttler = Throttler(100)
            >>> throttler.allow(10)
            True
            >>> throttler.allow(50)
            False
            >>> throttler.allow(110)
            True
        """
        if (
            self.last_execution_time == -1
            or current_time - self.last_execution_time >= self.limit
        ):
            self.last_execution_time = current_time
            return True

        return False