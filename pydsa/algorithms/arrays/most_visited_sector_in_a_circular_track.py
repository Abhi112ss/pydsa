METADATA = {
    "id": 1560,
    "name": "Most Visited Sector in a Circular Track",
    "slug": "most_visited_sector_in_a_circular_track",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "difference_array", "prefix_sum"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the sector in a circular track that is visited the most number of times given a series of movements.",
}

def solve(sectors: list[int], movements: list[int]) -> int:
    """
    Finds the sector that is visited the most number of times in a circular track.

    Args:
        sectors: A list of integers representing the sectors in the circular track.
        movements: A list of integers representing the number of sectors moved in each step.

    Returns:
        The index of the sector that was visited the most. If there is a tie, 
        returns the smallest index.

    Examples:
        >>> solve([1, 2, 3], [1, 1, 1])
        0
        >>> solve([1, 2, 3, 4], [1, 2, 1])
        2
    """
    n = len(sectors)
    # Use a difference array to handle range updates efficiently.
    # diff[i] stores the change in visits at index i.
    diff = [0] * (n + 1)

    current_pos = 0
    for move in movements:
        # Calculate the target position after the move.
        # Since it's circular, we use modulo.
        next_pos = (current_pos + move) % n
        
        # We need to mark the range [current_pos, next_pos] as visited.
        # Because it's circular, the range might wrap around.
        if current_pos <= next_pos:
            # Standard range update: increment start, decrement after end.
            diff[current_pos] += 1
            diff[next_pos + 1] -= 1
        else:
            # Wrap-around case: update [current_pos, n-1] and [0, next_pos].
            # Part 1: current_pos to end of array
            diff[current_pos] += 1
            diff[n] -= 1
            # Part 2: start of array to next_pos
            diff[0] += 1
            diff[next_pos + 1] -= 1
            
        current_pos = next_pos

    # Reconstruct the actual visit counts using prefix sums.
    max_visits = -1
    best_sector = -1
    current_visits = 0
    
    for i in range(n):
        current_visits += diff[i]
        if current_visits > max_visits:
            max_visits = current_visits
            best_sector = i
            
    return best_sector
