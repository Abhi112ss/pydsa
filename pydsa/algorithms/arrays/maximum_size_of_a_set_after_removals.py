METADATA = {
    "id": 3002,
    "name": "Maximum Size of a Set After Removals",
    "slug": "maximum-size-of-a-set-after-removals",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "greedy"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum size of a set after removing exactly k elements such that the remaining elements form a set of maximum possible size.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Calculates the maximum size of a set after removing exactly k elements.
    
    The problem asks us to remove k elements. To keep the set size as large 
    as possible, we want to remove elements that are 'duplicates' first. 
    If we remove a duplicate, the number of unique elements in the set 
    remains unchanged. If we are forced to remove a unique element, 
    the set size decreases.

    Args:
        nums: A list of integers.
        k: The number of elements to remove.

    Returns:
        The maximum size of the set after k removals.

    Examples:
        >>> solve([4, 3, 2, 3, 3], 2)
        2
        >>> solve([1, 2, 3, 4], 2)
        2
        >>> solve([1, 1, 1, 1], 2)
        1
    """
    # Count the frequency of each number
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1
    
    unique_elements_count = len(counts)
    # Total number of 'extra' elements (duplicates) available to be removed
    # without reducing the unique count.
    total_elements = len(nums)
    extra_elements = total_elements - unique_elements_count
    
    # If we can satisfy the removal requirement using only duplicates
    if k <= extra_elements:
        # The set size remains the number of unique elements
        return unique_elements_count
    else:
        # We exhausted all duplicates and still need to remove more elements.
        # Each additional removal must take away a unique element.
        remaining_removals_needed = k - extra_elements
        return unique_elements_count - remaining_removals_needed
