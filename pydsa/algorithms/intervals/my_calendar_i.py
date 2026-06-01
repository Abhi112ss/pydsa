METADATA = {
    "id": 729,
    "name": "My Calendar I",
    "slug": "my-calendar-i",
    "category": "Design",
    "aliases": [],
    "tags": ["binary_search_tree", "ordered_map", "binary_search"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Design a class that manages calendar events and determines if a new event can be added without overlapping existing ones.",
}

import bisect

class MyCalendar:
    """
    A class to manage calendar events and prevent overlaps.
    
    Uses a sorted list of event start times to perform binary search 
    for efficient overlap detection.
    """

    def __init__(self) -> None:
        """Initializes the calendar with an empty list of events."""
        # Stores tuples of (start, end) sorted by start time
        self.calendar: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        """
        Attempts to book an event.

        Args:
            start (int): The start time of the event.
            end (int): The end time of the event.

        Returns:
            bool: True if the event was successfully booked, False otherwise.

        Examples:
            >>> obj = MyCalendar()
            >>> obj.book(10, 20)
            True
            >>> obj.book(15, 25)
            False
            >>> obj.book(20, 30)
            True
        """
        # Find the index where this event would be inserted to maintain order
        # bisect_left returns the leftmost insertion point for (start, end)
        idx = bisect.bisect_left(self.calendar, (start, end))

        # Check overlap with the next event (the one at the insertion index)
        # An overlap occurs if the new event's end is greater than the next event's start
        if idx < len(self.calendar) and end > self.calendar[idx][0]:
            return False

        # Check overlap with the previous event (the one before the insertion index)
        # An overlap occurs if the previous event's end is greater than the new event's start
        if idx > 0 and self.calendar[idx - 1][1] > start:
            return False

        # No overlap found, insert the event into the sorted list
        self.calendar.insert(idx, (start, end))
        return True

def solve() -> None:
    """
    Example usage of the MyCalendar class.
    """
    calendar = MyCalendar()
    print(calendar.book(10, 20))  # Expected: True
    print(calendar.book(15, 25))  # Expected: False
    print(calendar.book(20, 30))  # Expected: True
