METADATA = {
    "id": 2222,
    "name": "Number of Ways to Select Buildings",
    "slug": "number-of-ways-to-select-buildings",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "prefix_sum", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of triplets (i, j, k) such that i < j < k and buildings[i] != buildings[j] and buildings[j] != buildings[k].",
}

def solve(buildings: list[int]) -> int:
    """
    Calculates the number of ways to select three buildings such that the 
    pattern is either 0-1-0 or 1-0-1.

    Args:
        buildings: A list of integers where each element is either 0 or 1.

    Returns:
        The total number of valid triplets (i, j, k) with i < j < k 
        and buildings[i] != buildings[j] and buildings[j] != buildings[k].

    Examples:
        >>> solve([0, 1, 0, 1, 0])
        4
        >>> solve([1, 1, 1, 1])
        0
    """
    total_zeros = buildings.count(0)
    total_ones = len(buildings) - total_zeros
    
    count_zeros_seen = 0
    count_ones_seen = 0
    total_ways = 0
    
    for building in buildings:
        if building == 0:
            # If current building is 0, it can be the middle element 'j' 
            # in a 1-0-1 pattern.
            # The number of ways is (ones seen before) * (ones remaining after).
            ones_remaining = total_ones - count_ones_seen
            total_ways += count_ones_seen * ones_remaining
            count_zeros_seen += 1
        else:
            # If current building is 1, it can be the middle element 'j' 
            # in a 0-1-0 pattern.
            # The number of ways is (zeros seen before) * (zeros remaining after).
            zeros_remaining = total_zeros - count_zeros_seen
            total_ways += count_zeros_seen * zeros_remaining
            count_ones_seen += 1
            
    return total_ways
