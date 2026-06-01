METADATA = {
    "id": 3020,
    "name": "Find the Maximum Number of Elements in Subset",
    "slug": "find-the-maximum-number-of-elements-in-subset",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "greedy", "math"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum size of a subset where every element x satisfies the condition that x + 1 is also in the subset, or x is the maximum element.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the maximum number of elements in a subset such that for every element x 
    in the subset, either x + 1 is also in the subset or x is the maximum element 
    of the subset.

    Args:
        nums: A list of integers.

    Returns:
        The maximum size of such a subset.

    Examples:
        >>> solve([1, 2, 3, 3, 4])
        4
        >>> solve([1, 1, 1])
        1
        >>> solve([1, 2, 4, 5, 6])
        3
    """
    if not nums:
        return 0

    # Count frequencies of each number to handle duplicates and existence checks
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Sort unique keys to process consecutive sequences
    unique_nums = sorted(counts.keys())
    
    max_subset_size = 0
    current_subset_size = 0
    
    for i in range(len(unique_nums)):
        # If current number is consecutive to the previous one, extend the sequence
        if i > 0 and unique_nums[i] == unique_nums[i - 1] + 1:
            current_subset_size += counts[unique_nums[i]]
        else:
            # Otherwise, start a new sequence with the current number's frequency
            current_subset_size = counts[unique_nums[i]]
        
        # Update the global maximum found so far
        if current_subset_size > max_subset_size:
            max_subset_size = current_subset_size

    # Special case: If all numbers are isolated, the max subset is the max frequency of a single number
    # However, the logic above already handles this by initializing current_subset_size 
    # to counts[unique_nums[i]] when a sequence breaks.
    
    return max_subset_size
