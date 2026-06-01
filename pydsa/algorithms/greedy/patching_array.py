METADATA = {
    "id": 330,
    "name": "Patching Array",
    "slug": "patching-array",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "math"],
    "difficulty": "hard",
    "time_complexity": "O(m + log n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of patches needed to make an array contain every number in the range [1, n].",
}

def solve(nums: list[int], n: int) -> int:
    """
    Finds the minimum number of patches required to cover the range [1, n].

    Args:
        nums: A sorted list of integers.
        n: The upper bound of the range to cover.

    Returns:
        The minimum number of patches needed.

    Examples:
        >>> solve([1, 3], 6)
        1
        >>> solve([1, 5, 10], 20)
        2
    """
    patches = 0
    # 'miss' represents the smallest integer that we cannot currently form.
    # We can currently form all integers in the range [1, miss - 1].
    miss = 1
    index = 0
    array_length = len(nums)

    while miss <= n:
        if index < array_length and nums[index] <= miss:
            # If the current number in the array is within our reachable range,
            # we use it to extend our range.
            miss += nums[index]
            index += 1
        else:
            # If the current number is too large or we've exhausted the array,
            # we must patch the array with 'miss' itself.
            # This is the most efficient patch because it doubles our reachable range.
            patches += 1
            miss += miss

    return patches
