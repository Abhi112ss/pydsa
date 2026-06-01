METADATA = {
    "id": 1550,
    "name": "Three Consecutive Odds",
    "slug": "three-consecutive-odds",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Determine if there are three consecutive odd integers in an array.",
}

def solve(nums: list[int]) -> bool:
    """
    Checks if the input list contains at least three consecutive odd integers.

    Args:
        nums: A list of integers.

    Returns:
        True if there are three consecutive odd numbers, False otherwise.

    Examples:
        >>> solve([1, 2, 3, 4, 5, 6, 7])
        False
        >>> solve([2, 3, 5, 7, 9])
        True
        >>> solve([1, 1, 2, 1, 1])
        False
    """
    consecutive_odds_count = 0

    for number in nums:
        # Check if the current number is odd using the modulo operator
        if number % 2 != 0:
            consecutive_odds_count += 1
            # If we reach the threshold of 3, we can return True immediately
            if consecutive_odds_count == 3:
                return True
        else:
            # Reset the counter if an even number is encountered
            consecutive_odds_count = 0

    return False
