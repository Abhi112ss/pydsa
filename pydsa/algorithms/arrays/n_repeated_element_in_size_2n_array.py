METADATA = {
    "id": 961,
    "name": "N-Repeated Element in Size 2N Array",
    "slug": "n-repeated-element-in-size-2n-array",
    "category": "Array",
    "aliases": [],
    "tags": ["hash_map", "counting", "array"],
    "difficulty": "easy",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the element that appears n times in an array of size 2n.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the element that appears n times in an array of size 2n.

    Args:
        nums: A list of integers of size 2n where one element is repeated n times.

    Returns:
        The integer that is repeated n times.

    Examples:
        >>> solve([1, 2, 1, 2, 1, 2])
        1
        >>> solve([1, 1, 2, 2, 3, 3, 4, 4, 4, 4])
        4
    """
    counts: dict[int, int] = {}
    target_count: int = len(nums) // 2

    for num in nums:
        # Increment the frequency count for the current number
        counts[num] = counts.get(num, 0) + 1
        
        # If the count reaches n, we have found our repeated element
        if counts[num] == target_count:
            return num

    # Fallback return (though problem guarantees a solution)
    return -1
