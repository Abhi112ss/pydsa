METADATA = {
    "id": 1845,
    "name": "Seat Reservation Manager",
    "slug": "seat-reservation-manager",
    "category": "Design",
    "aliases": [],
    "tags": ["heap", "priority_queue", "design"],
    "difficulty": "medium",
    "time_complexity": "O(log n)",
    "space_complexity": "O(n)",
    "description": "Design a system to manage seat reservations using a min-heap to always provide the smallest available seat number.",
}

import heapq

class SeatReservationManager:
    """
    A manager for seat reservations that ensures the smallest available 
    seat number is always provided first.
    """

    def __init__(self, n: int):
        """
        Initializes the manager with n seats.

        Args:
            n (int): The total number of seats available.
        """
        # We use a min-heap to store available seat numbers.
        # Initially, all seats from 1 to n are available.
        self.available_seats = list(range(1, n + 1))
        heapq.heapify(self.available_seats)
        self.total_seats = n

    def reserve(self, count: int) -> list[int]:
        """
        Reserves the smallest available seat numbers.

        Args:
            count (int): The number of seats to reserve.

        Returns:
            list[int]: A list of reserved seat numbers.

        Examples:
            >>> manager = SeatReservationManager(10)
            >>> manager.reserve(3)
            [1, 2, 3]
            >>> manager.reserve(2)
            [4, 5]
        """
        reserved = []
        # Extract the smallest element from the heap 'count' times.
        # Each pop operation takes O(log n) time.
        for _ in range(count):
            if self.available_seats:
                reserved.append(heapq.heappop(self.available_seats))
            else:
                # This case handles if more seats are requested than available,
                # though problem constraints usually imply valid requests.
                break
        return reserved

def solve():
    """
    Example usage of the SeatReservationManager.
    """
    # Example 1
    manager1 = SeatReservationManager(10)
    print(f"Reserve 3: {manager1.reserve(3)}")  # Expected: [1, 2, 3]
    print(f"Reserve 2: {manager1.reserve(2)}")  # Expected: [4, 5]
    print(f"Reserve 5: {manager1.reserve(5)}")  # Expected: [6, 7, 8, 9, 10]
    print(f"Reserve 1: {manager1.reserve(1)}")  # Expected: [] (no seats left)
