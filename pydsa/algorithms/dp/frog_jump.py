METADATA = {
    "id": 403,
    "name": "Frog Jump",
    "slug": "frog-jump",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "hash_set", "greedy"],
    "difficulty": "hard",
    "time_complexity": "O(n^2)",
    "space_complexity": "O(n^2)",
    "description": "Determine if a frog can reach the last stone in a series of jumps where each jump distance is k-1, k, or k+1 from the previous jump distance.",
}

def solve(stones: list[int]) -> bool:
    """
    Determines if the frog can reach the last stone in the stones list.

    The frog starts at the first stone with an initial jump distance of 0.
    From a stone at position 'current_pos' with a previous jump 'k', 
    the frog can jump to 'current_pos + k-1', 'current_pos + k', or 'current_pos + k+1'.

    Args:
        stones: A sorted list of integers representing the positions of the stones.

    Returns:
        True if the frog can reach the last stone, False otherwise.

    Examples:
        >>> solve([0, 1, 3, 5, 6, 8, 12, 17])
        True
        >>> solve([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17])
        False
    """
    if not stones:
        return False

    # Map stone position to a set of possible jump distances that landed on this stone.
    # This allows O(1) lookup for whether a stone exists and what jumps reached it.
    stone_reachability: dict[int, set[int]] = {stone: set() for stone in stones}
    
    # The first stone is at position 0. We simulate the first jump as 0 
    # so that the next jump can be 0+1=1.
    stone_reachability[stones[0]].add(0)

    for stone in stones:
        # For every stone we reach, try all possible next jumps
        for k in stone_reachability[stone]:
            # The frog can jump k-1, k, or k+1 units
            for next_jump in (k - 1, k, k + 1):
                # A jump must be at least 1 unit forward
                if next_jump > 0:
                    next_stone_pos = stone + next_jump
                    
                    # If the target position is a valid stone, record the jump distance
                    if next_stone_pos in stone_reachability:
                        stone_reachability[next_stone_pos].add(next_jump)
                        
                        # Optimization: If we reached the last stone, return True immediately
                        if next_stone_pos == stones[-1]:
                            return True

    # If we finish iterating and haven't returned True, the last stone is unreachable
    return False
