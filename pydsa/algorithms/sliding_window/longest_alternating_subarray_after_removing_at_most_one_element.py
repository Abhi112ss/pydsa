METADATA = {
    "id": 3830,
    "name": "Longest Alternating Subarray After Removing At Most One Element",
    "slug": "longest_alternating_subarray_after_removing_at_most_one_element",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["sliding_window", "dp", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the length of the longest alternating subarray possible after removing at most one element from the original array.",
}

def solve(nums: list[int]) -> int:
    """
    Finds the length of the longest alternating subarray after removing at most one element.
    An alternating subarray is defined by the property that adjacent elements have different signs.
    Note: In the context of this problem, 'alternating' usually refers to the sign pattern 
    (positive/negative) or parity. Based on standard LeetCode patterns for this description, 
    we assume alternating means nums[i] * nums[i+1] < 0.

    Args:
        nums: A list of integers.

    Returns:
        The length of the longest alternating subarray after removing at most one element.

    Examples:
        >>> solve([1, -1, 1, -1, 1])
        5
        >>> solve([1, 1, 1, -1, 1])
        4
    """
    n = len(nums)
    if n <= 1:
        return n

    def is_alternating(a: int, b: int) -> bool:
        # Check if signs are different (one positive, one negative)
        # 0 is treated as neither, but usually problems define it specifically.
        # Standard alternating sign check:
        return (a > 0 and b < 0) or (a < 0 and b > 0)

    # left[i] stores the length of the longest alternating subarray ending at index i
    left = [1] * n
    for i in range(1, n):
        if is_alternating(nums[i-1], nums[i]):
            left[i] = left[i-1] + 1
        else:
            left[i] = 1

    # right[i] stores the length of the longest alternating subarray starting at index i
    right = [1] * n
    for i in range(n - 2, -1, -1):
        if is_alternating(nums[i], nums[i+1]):
            right[i] = right[i+1] + 1
        else:
            right[i] = 1

    # Case 1: No element is removed.
    max_len = max(left)

    # Case 2: Remove exactly one element at index i.
    # We check if nums[i-1] and nums[i+1] can form an alternating pair.
    for i in range(n):
        # If we remove the first element
        if i == 0:
            max_len = max(max_len, right[1] if n > 1 else 0)
        # If we remove the last element
        elif i == n - 1:
            max_len = max(max_len, left[n-2])
        else:
            # If we remove element at index i, check if i-1 and i+1 can connect
            # The length would be (alternating sequence ending at i-1) + (alternating sequence starting at i+1)
            # ONLY if nums[i-1] and nums[i+1] satisfy the alternating condition.
            if is_alternating(nums[i-1], nums[i+1]):
                max_len = max(max_len, left[i-1] + right[i+1])
            else:
                # If they don't connect, the best we can do is the max of the two sides
                max_len = max(max_len, left[i-1], right[i+1])

    return max_len
