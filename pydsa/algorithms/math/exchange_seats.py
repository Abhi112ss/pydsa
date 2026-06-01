METADATA = {
    "id": 626,
    "name": "Exchange Seats",
    "slug": "exchange-seats",
    "category": "Array",
    "aliases": [],
    "tags": ["logic", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Swap adjacent seats in a row, ensuring the last person remains if the total count is odd.",
}

def solve(seats: list[int]) -> list[int]:
    """
    Swaps adjacent seats in a row. If the number of seats is odd, 
    the last person stays in their seat.

    Args:
        seats: A list of integers representing the IDs of people in seats.

    Returns:
        A list of integers representing the new arrangement of seats.

    Examples:
        >>> solve([1, 2, 3, 4])
        [2, 1, 4, 3]
        >>> solve([1, 2, 3, 4, 5])
        [2, 1, 4, 3, 5]
    """
    n = len(seats)
    # Create a copy to avoid mutating the input list in-place if required by caller
    # though in many LeetCode contexts, in-place is acceptable.
    result = list(seats)

    # Iterate through the list with a step of 2 to process pairs
    for i in range(0, n - 1, 2):
        # Swap the current seat with the next seat
        result[i], result[i + 1] = result[i + 1], result[i]

    # If n is odd, the loop stops at n-2, leaving the last element untouched.
    # This correctly handles the boundary condition where the last person has no partner.
    return result
