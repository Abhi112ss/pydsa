METADATA = {
    "id": 2856,
    "name": "Minimum Array Length After Pair Removals",
    "slug": "minimum-array-length-after-pair-removals",
    "category": "Array",
    "aliases": [],
    "tags": ["arrays", "greedy", "hash_map"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum possible length of an array after repeatedly removing two different elements.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum possible length of the array after removing pairs of different elements.

    The core logic relies on the observation that if one element appears more than 
    half the time (majority element), it will dictate the remaining length. 
    Otherwise, we can pair almost all elements, leaving either 0 or 1 element.

    Args:
        nums: A list of integers representing the array.

    Returns:
        The minimum length of the array after all possible valid removals.

    Examples:
        >>> solve([1, 2, 3, 4, 5])
        1
        >>> solve([1, 1, 2, 2, 2])
        1
        >>> solve([1, 1, 1, 1])
        4
    """
    if not nums:
        return 0

    # Count frequencies of each number
    counts: dict[int, int] = {}
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    total_elements = len(nums)
    max_frequency = 0
    
    # Find the frequency of the most frequent element
    for freq in counts.values():
        if freq > max_frequency:
            max_frequency = freq

    # Case 1: A single element appears more than half the time.
    # Even if we pair every other element with this majority element,
    # some instances of the majority element will remain.
    # Remaining = max_frequency - (total_elements - max_frequency)
    if max_frequency > total_elements // 2:
        return max_frequency - (total_elements - max_frequency)

    # Case 2: No element is a strict majority.
    # We can pair elements such that we are left with either 0 (if total is even)
    # or 1 (if total is odd) element.
    return total_elements % 2
