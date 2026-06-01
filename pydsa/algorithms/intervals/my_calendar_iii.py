METADATA = {
    "id": 732,
    "name": "My Calendar III",
    "slug": "my-calendar-iii",
    "category": "Design",
    "aliases": [],
    "tags": ["sweep_line", "ordered_map", "segment_tree"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Design a class that tracks overlapping intervals and returns the maximum number of concurrent events.",
}

import bisect

class MyCalendarThree:
    """
    A class that implements a calendar system to track the maximum number 
    of concurrent events (k-booking).
    """

    def __init__(self) -> None:
        """
        Initializes the calendar with an empty timeline.
        We use a sorted list of keys to simulate a sorted map for the sweep-line algorithm.
        """
        # delta_map stores the net change in active events at specific time points.
        # key: time, value: change in number of active events.
        self.delta_map: dict[int, int] = {}
        # sorted_times maintains the keys of delta_map in ascending order.
        self.sorted_times: list[int] = []

    def book(self, start: int, end: int) -> int:
        """
        Books a new event and returns the maximum number of concurrent events.

        Args:
            start (int): The start time of the event.
            end (int): The end time of the event.

        Returns:
            int: The maximum number of overlapping events (k-booking) at any point.

        Examples:
            >>> calendar = MyCalendarThree()
            >>> calendar.book(10, 20)
            1
            >>> calendar.book(50, 60)
            1
            >>> calendar.book(10, 40)
            2
            >>> calendar.book(5, 15)
            3
        """
        # Update the delta at the start time (+1 event)
        self._update_delta(start, 1)
        # Update the delta at the end time (-1 event)
        self._update_delta(end, -1)

        # Sweep-line algorithm: iterate through sorted time points to find the peak
        max_overlap = 0
        current_overlap = 0
        for time in self.sorted_times:
            current_overlap += self.delta_map[time]
            if current_overlap > max_overlap:
                max_overlap = current_overlap
        
        return max_overlap

    def _update_delta(self, time: int, delta: int) -> None:
        """
        Helper to update the delta map and maintain the sorted order of keys.

        Args:
            time (int): The timestamp to update.
            delta (int): The value to add to the existing delta.
        """
        if time in self.delta_map:
            self.delta_map[time] += delta
        else:
            self.delta_map[time] = delta
            # Maintain sorted order of keys for the sweep-line process
            bisect.insort(self.sorted_times, time)
        
        # If a delta becomes zero, we could technically remove it, 
        # but for simplicity in this implementation, we keep it.
        # However, if we wanted to optimize space, we'd remove keys where delta == 0.

def solve() -> None:
    """
    Example usage of the MyCalendarThree class.
    """
    calendar = MyCalendarThree()
    print(calendar.book(10, 20))  # Expected: 1
    print(calendar.book(50, 60))  # Expected: 1
    print(calendar.book(10, 40))  # Expected: 2
    print(calendar.book(5, 15))   # Expected: 3
