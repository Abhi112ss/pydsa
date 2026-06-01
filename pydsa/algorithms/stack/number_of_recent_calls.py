METADATA = {
    "id": 933,
    "name": "Number of Recent Calls",
    "slug": "number_of_recent_calls",
    "category": "Design",
    "aliases": [],
    "tags": ["queue", "design"],
    "difficulty": "medium",
    "time_complexity": "O(1) amortized",
    "space_complexity": "O(n)",
    "description": "Implements a RecentCounter that returns the number of calls within the past 3000 milliseconds."
}

from collections import deque
import sys

class RecentCounter:
    """Keeps track of recent call timestamps and returns the count within a 3000 ms window."""

    def __init__(self) -> None:
        # Store timestamps in increasing order; older entries are removed lazily.
        self._timestamps: deque[int] = deque()

    def ping(self, timestamp: int) -> int:
        """
        Record a new call at `timestamp` and return the number of calls that have
        occurred in the inclusive range [timestamp - 3000, timestamp].

        Args:
            timestamp: The current call time in milliseconds. Timestamps are
                       strictly increasing across calls.

        Returns:
            The count of calls within the last 3000 ms, including the current one.
        """
        self._timestamps.append(timestamp)

        # Remove timestamps that are older than the allowed 3000 ms window.
        while self._timestamps and self._timestamps[0] < timestamp - 3000:
            self._timestamps.popleft()

        return len(self._timestamps)


def solve() -> None:
    """
    Reads a sequence of timestamps from standard input, invokes `RecentCounter.ping`
    for each, and prints the resulting counts.

    Input format:
        The first line contains an integer `n`, the number of timestamps.
        The next `n` lines each contain a single integer timestamp.

    Output format:
        `n` integers separated by spaces, each representing the result of a `ping`
        call for the corresponding timestamp.

    Example:
        Input:
            5
            1
            300
            3001
            3002
            7000
        Output:
            1 2 3 3 2
    """
    data = sys.stdin.read().strip().split()
    if not data:
        return

    n = int(data[0])
    timestamps = list(map(int, data[1:1 + n]))

    counter = RecentCounter()
    results: list[int] = []

    for ts in timestamps:
        results.append(counter.ping(ts))

    sys.stdout.write(" ".join(map(str, results)))
