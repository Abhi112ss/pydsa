METADATA = {
    "id": 1005,
    "name": "Maximize Sum Of Array After K Negations",
    "slug": "maximize-sum-of-array-after-k-negations",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "sorting", "heap"],
    "difficulty": "medium",
    "time_complexity": "O(n log n)",
    "space_complexity": "O(1)",
    "description": "Maximize the sum of an array after performing exactly k negations on array elements.",
}

def solve(nums: list[int], k: int) -> int:
    """
    Maximizes the sum of the array after performing exactly k negations.

    The strategy is to greedily negate the most negative numbers first to 
    increase the sum as much as possible. If k remains positive after all 
    negative numbers are flipped, we handle the remaining k by repeatedly 
    negating the element with the smallest absolute value.

    Args:
        nums: A list of integers.
        k: The number of negations to perform.

    Returns:
        The maximum possible sum of the array after k negations.

    Examples:
        >>> solve([4, 2, 3], 1)
        5
        >>> solve([3, -1, 0, 2], 3)
        6
        >>> solve([2, -3, -1, 5, -4], 2)
        13
    """
    # Sort the array to easily access the smallest (most negative) numbers
    nums.sort()

    # Step 1: Negate as many negative numbers as possible, up to k times
    for i in range(len(nums)):
        if nums[i] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
        else:
            break

    # Step 2: If k is still positive and odd, we must negate one more time.
    # We choose the smallest element in the modified array to minimize the loss.
    # If k is even, negating the same element twice results in no change.
    if k % 2 == 1:
        # Re-sorting or finding min is necessary because a previously 
        # negative number might now be the smallest positive number.
        nums.sort()
        nums[0] = -nums[0]

    return sum(nums)
