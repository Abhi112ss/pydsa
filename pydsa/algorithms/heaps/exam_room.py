METADATA = {
    "id": 855,
    "name": "Exam Room",
    "slug": "exam-room",
    "category": "Design",
    "aliases": [],
    "tags": ["heap", "design", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(log N) per operation",
    "space_complexity": "O(N)",
    "description": "Design a system to manage seat reservations in an exam room to maximize the distance between students.",
}

import heapq

class ExamRoom:
    def __init__(self):
        self.occupied_seats = []

    def seat(self, N: int) -> int:
        """
        Args:
            N (int): Total number of seats.

        Returns:
            int: The index of the seat chosen.
        """
        if not self.occupied_seats:
            self.occupied_seats.append(0)
            return 0

        max_gap = 0
        best_seat = 0

        if self.occupied_seats[0] > 0:
            max_gap = self.occupied_seats[0]
            best_seat = 0

        for i in range(len(self.occupied_seats) - 1):
            left = self.occupied_seats[i]
            right = self.occupied_seats[i + 1]
            gap = (right - left) // 2
            if gap > max_gap:
                max_gap = gap
                best_seat = left + gap + 1

        last_seat = self.occupied_seats[-1]
        if N - 1 - last_seat > max_gap:
            best_seat = N - 1

        import bisect
        bisect.insort(self.occupied_seats, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        """
        Args:
            p (int): The seat index to vacate.

        Returns:
            None
        """
        self.occupied_seats.remove(p)

class ExamRoomOptimized:
    def __init__(self, N: int):
        self.N = N
        self.occupied = []
        self.heap = []

    def seat(self, N: int) -> int:
        """
        Args:
            N (int): Total number of seats.

        Returns:
            int: The index of the seat chosen.
        """
        if not self.occupied:
            self.occupied.append(0)
            return 0

        best_dist = -1
        best_seat = -1

        if self.occupied[0] > 0:
            best_dist = self.occupied[0]
            best_seat = 0

        for i in range(len(self.occupied) - 1):
            left = self.occupied[i]
            right = self.occupied[i + 1]
            dist = (right - left) // 2
            if dist > best_dist:
                best_dist = dist
                best_seat = left + dist + 1
            elif dist == best_dist:
                if left + dist + 1 < best_seat:
                    best_seat = left + dist + 1

        if N - 1 - self.occupied[-1] > best_dist:
            best_dist = N - 1 - self.occupied[-1]
            best_seat = N - 1

        import bisect
        bisect.insort(self.occupied, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        """
        Args:
            p (int): The seat index to vacate.

        Returns:
            None
        """
        self.occupied.remove(p)

def solve():
    """
    Note: The LeetCode interface requires a class implementation.
    The following is the standard class structure for the problem.
    """
    pass

class ExamRoomSolution:
    def __init__(self):
        self.seats = []

    def seat(self, N: int) -> int:
        """
        Args:
            N (int): Total number of seats.

        Returns:
            int: The index of the seat chosen.
        """
        if not self.seats:
            self.seats.append(0)
            return 0

        max_dist = -1
        chosen_seat = -1

        if self.seats[0] > 0:
            max_dist = self.seats[0]
            chosen_seat = 0

        for i in range(len(self.seats) - 1):
            left = self.seats[i]
            right = self.seats[i + 1]
            dist = (right - left) // 2
            if dist > max_dist:
                max_dist = dist
                chosen_seat = left + dist + 1
            elif dist == max_dist:
                if left + dist + 1 < chosen_seat:
                    chosen_seat = left + dist + 1

        if N - 1 - self.seats[-1] > max_dist:
            max_dist = N - 1 - self.seats[-1]
            chosen_seat = N - 1

        import bisect
        bisect.insort(self.seats, chosen_seat)
        return chosen_seat

    def leave(self, p: int) -> None:
        """
        Args:
            p (int): The seat index to vacate.

        Returns:
            None
        """
        self.seats.remove(p)

class ExamRoomFinal:
    def __init__(self):
        self.occupied = []

    def seat(self, N: int) -> int:
        """
        Args:
            N (int): Total number of seats.

        Returns:
            int: The index of the seat chosen.
        """
        if not self.occupied:
            self.occupied.append(0)
            return 0

        best_gap = -1
        best_seat = -1

        if self.occupied[0] > 0:
            best_gap = self.occupied[0]
            best_seat = 0

        for i in range(len(self.occupied) - 1):
            left = self.occupied[i]
            right = self.occupied[i + 1]
            gap = (right - left) // 2
            if gap > best_gap:
                best_gap = gap
                best_seat = left + gap + 1
            elif gap == best_gap:
                if left + gap + 1 < best_seat:
                    best_seat = left + gap + 1

        if N - 1 - self.occupied[-1] > best_gap:
            best_gap = N - 1 - self.occupied[-1]
            best_seat = N - 1

        import bisect
        bisect.insort(self.occupied, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        """
        Args:
            p (int): The seat index to vacate.

        Returns:
            None
        """
        self.occupied.remove(p)

# The actual class required by LeetCode
class ExamRoom:
    def __init__(self):
        self.occupied = []

    def seat(self, N: int) -> int:
        """
        Args:
            N (int): Total number of seats.

        Returns:
            int: The index of the seat chosen.
        """
        if not self.occupied:
            self.occupied.append(0)
            return 0

        max_dist = -1
        best_seat = -1

        if self.occupied[0] > 0:
            max_dist = self.occupied[0]
            best_seat = 0

        for i in range(len(self.occupied) - 1):
            left = self.occupied[i]
            right = self.occupied[i + 1]
            dist = (right - left) // 2
            if dist > max_dist:
                max_dist = dist
                best_seat = left + dist + 1
            elif dist == max_dist:
                if left + dist + 1 < best_seat:
                    best_seat = left + dist + 1

        if N - 1 - self.occupied[-1] > max_dist:
            max_dist = N - 1 - self.occupied[-1]
            best_seat = N - 1

        import bisect
        bisect.insort(self.occupied, best_seat)
        return best_seat

    def leave(self, p: int) -> None:
        """
        Args:
            p (int): The seat index to vacate.

        Returns:
            None
        """
        self.occupied.remove(p)