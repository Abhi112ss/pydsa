METADATA = {
    "id": 359,
    "name": "Logger Rate Limiter",
    "slug": "logger_rate_limiter",
    "category": "Design",
    "aliases": ["Logger Rate Limiter"],
    "tags": ["design", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(n)",
    "description": "Design a logger system that receives a stream of messages with timestamps, printing each unique message at most once every 10 seconds.",
}

class Logger:
    def __init__(self) -> None:
        # Maps each message to the earliest timestamp at which it can be printed again
        self.message_next_allowed: dict[str, int] = {}

    def should_print_message(self, timestamp: int, message: str) -> bool:
        """
        Returns True if the message should be printed at the given timestamp,
        otherwise returns False.

        Args:
            timestamp: The current timestamp (non-negative integer, monotonically increasing).
            message: The message string to evaluate.

        Returns:
            True if the message should be printed, False if it was printed within the last 10 seconds.

        Examples:
            >>> logger = Logger()
            >>> logger.should_print_message(1, "foo")
            True
            >>> logger.should_print_message(2, "bar")
            True
            >>> logger.should_print_message(3, "foo")
            False
            >>> logger.should_print_message(8, "bar")
            False
            >>> logger.should_print_message(10, "foo")
            False
            >>> logger.should_print_message(11, "foo")
            True
        """
        # Check if this message has been seen and is still within the 10-second cooldown
        if message in self.message_next_allowed and timestamp < self.message_next_allowed[message]:
            return False

        # Allow printing and record the next allowed timestamp (current + 10)
        self.message_next_allowed[message] = timestamp + 10
        return True


def solve(operations: list[str], arguments: list[list]) -> list:
    """
    Simulates a sequence of Logger operations and returns the results.

    Args:
        operations: List of operation names, e.g. ["Logger", "should_print_message", ...].
        arguments: List of argument lists for each operation, e.g. [[], [1, "foo"], ...].

    Returns:
        A list of results: None for "Logger" constructor, bool for "should_print_message".

    Examples:
        >>> solve(
        ...     ["Logger", "should_print_message", "should_print_message", "should_print_message", "should_print_message", "should_print_message", "should_print_message"],
        ...     [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
        ... )
        [None, True, True, False, False, False, True]
    """
    logger: Logger | None = None
    results: list = []

    for op, args in zip(operations, arguments):
        if op == "Logger":
            logger = Logger()
            results.append(None)
        elif op == "should_print_message":
            # logger is guaranteed to be initialized before this call
            results.append(logger.should_print_message(args[0], args[1]))

    return results