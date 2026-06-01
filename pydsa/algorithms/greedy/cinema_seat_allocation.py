METADATA = {
    "id": 1386,
    "name": "Cinema Seat Allocation",
    "slug": "cinema-seat-allocation",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "hash_map", "bit_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of available 4-seat blocks in a cinema row where seats 5, 6, 7, and 8 are empty.",
}

def solve(n: int, reserved_seats: list[int]) -> int:
    """
    Calculates the number of available 4-seat blocks (seats 5, 6, 7, and 8).

    A block is available only if none of the seats 5, 6, 7, or 8 are in the 
    reserved_seats list.

    Args:
        n: The total number of seats in the row.
        reserved_seats: A list of integers representing the indices of reserved seats.

    Returns:
        The number of available 4-seat blocks.

    Examples:
        >>> solve(10, [5, 6, 7, 8])
        0
        >>> solve(10, [1, 2, 3])
        1
        >>> solve(10, [5])
        0
    """
    # If the total number of seats is less than 8, no 4-seat block (5-8) can exist.
    if n < 8:
        return 0

    # Use a set for O(1) average time complexity lookups.
    # This is more efficient than checking 'if seat in reserved_seats' on a list.
    reserved_set = set(reserved_seats)

    # The target block is specifically seats 5, 6, 7, and 8.
    # We only need to check if any of these specific seats are present in the set.
    target_block = {5, 6, 7, 8}
    
    # Check if the intersection of the reserved seats and our target block is empty.
    # If the intersection is empty, it means none of the seats 5, 6, 7, or 8 are reserved.
    if not target_block.intersection(reserved_set):
        return 1
    
    return 0
