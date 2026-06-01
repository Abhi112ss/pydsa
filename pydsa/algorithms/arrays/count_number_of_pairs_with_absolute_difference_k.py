METADATA = {
    "id": 2006,
    "name": "Count Number of Pairs With Absolute Difference K",
    "slug": "count-number-of-pairs-with-absolute-difference-k",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "arrays", "counting"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Count the number of pairs (i, j) such that the absolute difference between nums[i] and nums[j] is exactly k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Counts the number of pairs (i, j) in the list such that |nums[i] - nums[j]| == k.

    Args:
        nums: A list of integers.
        k: The target absolute difference.

    Returns:
        The total count of pairs satisfying the condition.

    Examples:
        >>> solve([1, 2, 2, 1], 1)
        4
        >>> solve([1, 3], 3)
        0
    """
    # Frequency map to store the count of each number encountered so far
    frequency_map: dict[int, int] = {}
    pair_count: int = 0

    for num in nums:
        # If |num - x| = k, then x can be (num - k) or (num + k)
        # We check how many times these targets have appeared previously
        target_low = num - k
        target_high = num + k

        if target_low in frequency_map:
            pair_count += frequency_map[target_low]
        
        # If k is 0, target_low and target_high are the same, 
        # but the problem constraints usually imply k > 0 for this specific problem.
        # However, we handle it by checking target_high separately only if it's distinct.
        if k > 0 and target_high in frequency_map:
            pair_count += frequency_map[target_high]

        # Update the frequency of the current number in the map
        frequency_map[num] = frequency_map.get(num, 0) + 1

    return pair_count
