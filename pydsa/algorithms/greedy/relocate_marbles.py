METADATA = {
    "id": 2766,
    "name": "Relocate Marbles",
    "slug": "relocate_marbles",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of moves to relocate all marbles to the leftmost positions.",
}

def solve(marbles: list[int]) -> int:
    """
    Calculates the minimum number of moves to relocate all marbles to the leftmost positions.
    
    A move consists of shifting a marble from its current position to an adjacent position.
    The goal is to pack all marbles starting from index 0, 1, ..., k-1.

    Args:
        marbles: A list of integers where 1 represents a marble and 0 represents an empty space.

    Returns:
        The minimum number of moves required.

    Examples:
        >>> solve([1, 0, 1, 0, 1])
        3
        >>> solve([0, 0, 1, 1, 0, 1])
        6
        >>> solve([1, 1, 1])
        0
    """
    total_moves = 0
    # target_index tracks where the next marble should be placed (0, 1, 2...)
    target_index = 0
    
    for current_index, has_marble in enumerate(marbles):
        if has_marble == 1:
            # The number of moves to bring a marble from current_index to target_index
            # is simply the distance between them.
            total_moves += (current_index - target_index)
            
            # Increment target_index because the next marble found will occupy the next slot
            target_index += 1
            
    return total_moves
