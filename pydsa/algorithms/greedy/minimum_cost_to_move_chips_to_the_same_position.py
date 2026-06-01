METADATA = {
    "id": 1217,
    "name": "Minimum Cost to Move Chips to The Same Position",
    "slug": "minimum_cost_to_move_chips_to_the_same_position",
    "category": "array",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Compute the minimal cost to move all chips to a single position where moving by 2 is free and moving by 1 costs 1.",
}


def solve(chips: list[int]) -> int:
    """Calculate the minimum cost to move all chips to the same position.

    Args:
        chips: List of integer positions of the chips.

    Returns:
        Minimum total cost as an integer.

    Examples:
        >>> solve([1, 2, 3])
        1
        >>> solve([2, 2, 2, 3, 3])
        0
    """
    even_count = 0
    odd_count = 0
    for position in chips:
        if position % 2 == 0:
            even_count += 1  # chip is on an even position
        else:
            odd_count += 1   # chip is on an odd position
    # Chips on the same parity can be moved freely; move the smaller group
    return min(even_count, odd_count)