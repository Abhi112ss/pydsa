METADATA = {
    "id": 3595,
    "name": "Once Twice",
    "slug": "once_twice",
    "category": "Arrays",
    "aliases": [],
    "tags": ["arrays", "hash_map"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Return a list of elements that appear exactly once or exactly twice in the input array, maintaining their original relative order.",
}

def solve(nums: list[int]) -> list[int]:
    """
    Filters the input list to return elements that appear exactly once or twice.

    The function preserves the original relative order of the elements that 
    meet the criteria.

    Args:
        nums: A list of integers.

    Returns:
        A list of integers that appear either once or twice in the input list.

    Examples:
        >>> solve([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        [1, 2, 2]
        >>> solve([1, 1, 1, 2, 3, 3])
        [2, 3, 3]
    """
    # Step 1: Build a frequency map to count occurrences of each number
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # Step 2: Iterate through the original list to maintain relative order
    # and filter elements based on the frequency map
    result: list[int] = []
    for num in nums:
        # We only include the number if its total count is 1 or 2
        if counts[num] == 1 or counts[num] == 2:
            result.append(num)
            
    return result
