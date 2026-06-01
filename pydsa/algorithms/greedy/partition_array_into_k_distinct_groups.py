METADATA = {
    "id": 3659,
    "name": "Partition Array Into K-Distinct Groups",
    "slug": "partition-array-into-k-distinct-groups",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if an array can be partitioned into k groups such that each group contains distinct elements.",
}

def solve(nums: list[int], k: int) -> bool:
    """
    Determines if the array can be partitioned into k groups where each group 
    contains only distinct elements.

    The core logic relies on the Pigeonhole Principle: if any single element 
    appears more than k times, it is impossible to distribute those identical 
    elements into k groups without at least one group receiving the same 
    element twice.

    Args:
        nums: A list of integers representing the array to be partitioned.
        k: The number of groups to partition the array into.

    Returns:
        True if the array can be partitioned into k distinct groups, False otherwise.

    Examples:
        >>> solve([1, 2, 2, 3], 2)
        True
        >>> solve([1, 2, 2, 2, 3], 2)
        False
    """
    if not nums:
        return True
    
    # Frequency map to count occurrences of each number
    counts: dict[int, int] = {}
    
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        
        # If any element's frequency exceeds the number of available groups,
        # it's impossible to keep elements in each group distinct.
        if counts[num] > k:
            return False
            
    return True
