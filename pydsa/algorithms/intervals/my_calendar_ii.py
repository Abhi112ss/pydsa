METADATA = {
    "id": 731,
    "name": "My Calendar II",
    "slug": "my-calendar-ii",
    "category": "Design",
    "aliases": [],
    "tags": ["ordered_map", "sweep_line", "interval"],
    "difficulty": "medium",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n)",
    "description": "Design a class that allows booking events while preventing triple bookings.",
}

class MyCalendarTwo:
    def __init__(self) -> None:
        """
        Initializes the calendar object.
        
        We maintain two lists:
        1. `bookings`: Stores all successful single bookings.
        2. `overlaps`: Stores intervals that represent a double booking.
        """
        self.bookings: list[tuple[int, int]] = []
        self.overlaps: list[tuple[int, int]] = []

    def book(self, start: int, end: int) -> bool:
        """
        Attempts to book an event. Returns True if successful, False otherwise.

        Args:
            start (int): The start time of the event.
            end (int): The end time of the event.

        Returns:
            bool: True if the booking does not cause a triple booking, False otherwise.

        Examples:
            >>> calendar = MyCalendarTwo()
            >>> calendar.book(10, 20)
            True
            >>> calendar.book(50, 60)
            True
            >>> calendar.book(10, 40)
            True
            >>> calendar.book(5, 15)
            False
        """
        # 1. Check if the new booking overlaps with any existing double bookings.
        # If it does, this would create a triple booking, so we reject it.
        for overlap_start, overlap_end in self.overlaps:
            if start < overlap_end and end > overlap_start:
                return False

        # 2. If valid, check for new double bookings created by this single booking.
        # We compare the new booking against all previous single bookings.
        for booking_start, booking_end in self.bookings:
            if start < booking_end and end > booking_start:
                # Calculate the intersection of the two intervals
                new_overlap_start = max(start, booking_start)
                new_overlap_end = min(end, booking_end)
                self.overlaps.append((new_overlap_start, new_overlap_end))

        # 3. Add the current booking to the list of single bookings.
        self.bookings.append((start, end))
        return True

def solve() -> None:
    """
    Example driver function to demonstrate usage.
    """
    calendar = MyCalendarTwo()
    assert calendar.book(10, 20) is True
    assert calendar.book(50, 60) is True
    assert calendar.book(10, 40) is True
    assert calendar.book(5, 15) is False
    print("All test cases passed!")
