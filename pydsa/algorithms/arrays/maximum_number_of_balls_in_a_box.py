METADATA = {
    "id": 1742,
    "name": "Maximum Number of Balls in a Box",
    "slug": "maximum_number_of_balls_in_a_box",
    "category": "Array",
    "aliases": [],
    "tags": ["array", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum count of balls that share the same position.",
}


def solve(nums: list[int]) -> int:
    """Return the maximum number of balls that can be placed in any box.

    Args:
        nums: A list of integers where each integer represents the position of a ball.

    Returns:
        The largest count of balls that share the same position (i.e., the maximum
        frequency of any value in ``nums``).

    Examples:
        >>> solve([1,2,1,2,1,3,2])
        3
        >>> solve([5,5,5,5])
        4
        >>> solve([1,2,3,4])
        1
    """
    if not nums:
        return 0

    position_counts: dict[int, int] = {}
    for position in nums:
        # Increment the count for the current ball position
        position_counts[position] = position_counts.get(position, 0) + 1

    # The answer is the highest frequency among all positions
    max_balls_in_box = max(position_counts.values())
    return max_balls_in_box