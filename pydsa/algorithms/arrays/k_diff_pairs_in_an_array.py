METADATA = {
    "id": 532,
    "name": "K-diff Pairs in an Array",
    "slug": "k-diff-pairs-in-an-array",
    "category": "Hash Table",
    "aliases": [],
    "tags": ["hash_map", "two_pointer"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the number of unique pairs (nums[i], nums[j]) such that |nums[i] - nums[j]| = k.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Finds the number of unique k-diff pairs in the given array.

    A k-diff pair is a pair (nums[i], nums[j]) such that |nums[i] - nums[j]| = k.
    The pair (a, b) is considered the same as (b, a).

    Args:
        nums: A list of integers.
        k: The target absolute difference.

    Returns:
        The count of unique k-diff pairs.

    Examples:
        >>> solve([3, 1, 4, 1, 5], 2)
        2
        >>> solve([1, 2, 3, 4, 5], 1)
        4
        >>> solve([1, 3, 1, 5, 4], 0)
        1
    """
    if k < 0:
        return 0

    # Count the frequency of each number in the array
    frequency_map: dict[int, int] = {}
    for num in nums:
        frequency_map[num] = frequency_map.get(num, 0) + 1

    count = 0

    # Iterate through the unique numbers in the frequency map
    for num in frequency_map:
        if k > 0:
            # If k > 0, we look for a unique partner (num + k)
            # This ensures we only count each pair once
            if (num + k) in frequency_map:
                count += 1
        else:
            # If k == 0, a pair exists only if the number appears at least twice
            if frequency_map[num] > 1:
                count += 1

    return count
