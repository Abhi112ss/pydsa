METADATA = {
    "id": 346,
    "name": "Moving Average from Data Stream",
    "slug": "moving_average_from_data_stream",
    "category": "Design",
    "aliases": [],
    "tags": ["queue", "design", "sliding_window"],
    "difficulty": "easy",
    "time_complexity": "O(1)",
    "space_complexity": "O(w)",
    "description": "Calculate the moving average of the last size elements of a data stream.",
}


from collections import deque
from typing import Deque


class MovingAverage:
    """Calculate the moving average of the last *size* values in a stream.

    The class maintains a fixed‑size queue and a running sum so that each call to
    :meth:`next` updates the average in constant time.

    Example:
        >>> ma = MovingAverage(3)
        >>> ma.next(1)   # average of [1] => 1.0
        1.0
        >>> ma.next(10)  # average of [1, 10] => 5.5
        5.5
        >>> ma.next(3)   # average of [1, 10, 3] => 4.666666666666667
        4.666666666666667
        >>> ma.next(5)   # average of [10, 3, 5] => 6.0
        6.0
    """

    def __init__(self, size: int) -> None:
        """Initialize the moving average with a fixed window size.

        Args:
            size: The maximum number of recent values to consider for the average.
        """
        self._window_size: int = size
        self._values: Deque[int] = deque(maxlen=size)
        self._running_sum: int = 0

    def next(self, val: int) -> float:
        """Add a new value to the stream and return the current moving average.

        Args:
            val: The new integer value from the data stream.

        Returns:
            The average of the last *size* values (or fewer if fewer values have been seen).
        """
        if len(self._values) == self._window_size:
            # Remove the oldest value from the running sum before adding the new one.
            oldest_value = self._values.popleft()
            self._running_sum -= oldest_value
        self._values.append(val)
        self._running_sum += val
        current_average = self._running_sum / len(self._values)
        return current_average


def solve() -> None:
    """Demonstrate the usage of :class:`MovingAverage`.

    This function is not part of the LeetCode submission; it simply shows how the
    class can be instantiated and used. No input is read from stdin and nothing
    is printed to stdout.

    Example:
        >>> solve()  # runs the example usage in the docstring of MovingAverage
    """
    # Example usage (mirrors the docstring example)
    moving_average = MovingAverage(3)
    _ = moving_average.next(1)
    _ = moving_average.next(10)
    _ = moving_average.next(3)
    _ = moving_average.next(5)
    # The function intentionally does not produce output.