METADATA = {
    "id": 1186,
    "name": "Maximum Subarray Sum with One Deletion",
    "slug": "maximum-subarray-sum-with-one-deletion",
    "category": "Dynamic Programming",
    "aliases": [],
    "tags": ["dynamic_programming", "kadane", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the maximum sum of a non-empty subarray where you are allowed to delete at most one element.",
}

def solve(arr: list[int]) -> int:
    """
    Calculates the maximum subarray sum allowing for at most one deletion.

    Args:
        arr: A list of integers representing the input array.

    Returns:
        The maximum sum of a non-empty subarray after at most one deletion.

    Examples:
        >>> solve([1, -2, 0, 3])
        4
        >>> solve([1, -2, -2, 3])
        3
        >>> solve([-1, -1, -1, -1])
        -1
    """
    n = len(arr)
    if n == 1:
        return arr[0]

    # max_no_deletion[i] is the max sum of a subarray ending at index i with 0 deletions.
    # This is the standard Kadane's algorithm state.
    max_no_deletion = [0] * n
    
    # max_one_deletion[i] is the max sum of a subarray ending at index i with exactly 1 deletion.
    # A deletion at index i can happen in two ways:
    # 1. We already deleted an element before index i, so we must include arr[i].
    # 2. We delete the current element arr[i], so we take the max sum ending at i-1 with 0 deletions.
    max_one_deletion = [0] * n

    max_no_deletion[0] = arr[0]
    # We cannot have a "one deletion" subarray ending at index 0 that is non-empty 
    # and valid under the rule of "at most one deletion" if we consider the 
    # deletion to be the element itself (leaving an empty subarray).
    # However, the problem implies the resulting subarray must be non-empty.
    # We initialize with a very small number to represent an impossible state.
    max_one_deletion[0] = float('-inf')

    overall_max = arr[0]

    for i in range(1, n):
        # Standard Kadane's: either start a new subarray at i or extend the previous one.
        max_no_deletion[i] = max(arr[i], max_no_deletion[i - 1] + arr[i])
        
        # Two choices for one deletion ending at i:
        # 1. max_one_deletion[i-1] + arr[i]: We already deleted something, so we must take arr[i].
        # 2. max_no_deletion[i-1]: We delete the current element arr[i].
        max_one_deletion[i] = max(max_one_deletion[i - 1] + arr[i], max_no_deletion[i - 1])
        
        # Update the global maximum with both possibilities.
        overall_max = max(overall_max, max_no_deletion[i], max_one_deletion[i])

    return int(overall_max)
