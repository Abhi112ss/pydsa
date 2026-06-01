METADATA = {
    "id": 3140,
    "name": "Consecutive Available Seats II",
    "slug": "consecutive-available-seats-ii",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "sorting", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the largest number of consecutive available seats in a row given a list of occupied seats.",
}

def solve(n: int, occupied_seats: list[int]) -> int:
    """
    Finds the maximum number of consecutive available seats in a row of n seats.

    Args:
        n: The total number of seats in the row (1-indexed).
        occupied_seats: A list of integers representing the indices of occupied seats.

    Returns:
        The maximum number of consecutive available seats.

    Examples:
        >>> solve(10, [2, 5, 8])
        2
        >>> solve(5, [1, 5])
        3
        >>> solve(10, [])
        10
    """
    if not occupied_seats:
        return n

    # Sort the occupied seats to identify gaps between them
    sorted_seats = sorted(occupied_seats)
    max_gap = 0

    # 1. Check the gap before the first occupied seat
    # If the first occupied seat is at index 5, seats 1, 2, 3, 4 are free (4 seats)
    max_gap = max(max_gap, sorted_seats[0] - 1)

    # 2. Check gaps between consecutive occupied seats
    # If seats 2 and 5 are occupied, seats 3 and 4 are free (5 - 2 - 1 = 2 seats)
    for i in range(len(sorted_seats) - 1):
        gap = sorted_seats[i + 1] - sorted_seats[i] - 1
        if gap > max_gap:
            max_gap = gap

    # 3. Check the gap after the last occupied seat
    # If the last occupied seat is at index 8 and n is 10, seats 9 and 10 are free (10 - 8 = 2 seats)
    max_gap = max(max_gap, n - sorted_seats[-1])

    return max_gap
