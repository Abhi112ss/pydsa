METADATA = {
    "id": 1338,
    "name": "Reduce Array Size to The Half",
    "slug": "reduce-array-size-to-the-half",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "hash_map", "sorting"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of unique integers to remove so that at least half of the array elements are removed.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the minimum number of unique integers to remove to reduce the 
    array size by at least half.

    Args:
        arr: A list of integers representing the input array.

    Returns:
        The minimum number of unique integers to remove.

    Examples:
        >>> solve([3, 3, 3, 3, 5, 5, 5, 2, 2, 7])
        1
        >>> solve([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
        1
        >>> solve([1, 9])
        1
    """
    n = len(arr)
    target_to_remove = (n + 1) // 2  # Equivalent to math.ceil(n / 2)
    
    # Step 1: Count the frequency of each integer
    frequency_map: dict[int, int] = {}
    for num in arr:
        frequency_map[num] = frequency_map.get(num, 0) + 1
    
    # Step 2: Extract frequencies and sort them in descending order
    # We want to remove the most frequent numbers first to minimize the count of unique integers
    frequencies: list[int] = sorted(frequency_map.values(), reverse=True)
    
    removed_elements_count = 0
    unique_integers_removed = 0
    
    # Step 3: Greedily pick the largest frequencies until we meet the target
    for freq in frequencies:
        removed_elements_count += freq
        unique_integers_removed += 1
        
        if removed_elements_count >= target_to_remove:
            return unique_integers_removed
            
    return unique_integers_removed
