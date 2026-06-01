METADATA = {
    "id": 667,
    "name": "Beautiful Arrangement II",
    "slug": "beautiful-arrangement-ii",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "math", "two-pointers"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Construct an array of size n containing integers from 1 to n such that there are exactly k distinct absolute differences between adjacent elements.",
}

def solve(n: int, k: int) -> list[int]:
    """
    Constructs an array of size n with exactly k distinct absolute differences.

    The strategy uses a two-pointer approach to alternate between the smallest 
    and largest available numbers to create a sequence of unique differences. 
    Once k differences are satisfied, the remaining numbers are appended 
    linearly to avoid creating new differences.

    Args:
        n: The number of elements in the array (integers from 1 to n).
        k: The exact number of distinct absolute differences required.

    Returns:
        A list of integers of length n satisfying the condition.

    Examples:
        >>> solve(5, 2)
        [1, 3, 2, 4, 5]
        >>> solve(5, 3)
        [1, 5, 2, 4, 3]
    """
    if k == 0:
        return list(range(1, n + 1))

    result = []
    left = 1
    right = n
    
    # We use a two-pointer approach to pick elements from both ends.
    # This creates large, then smaller, then larger differences.
    # We only do this for the first k + 1 elements to satisfy k differences.
    for i in range(k + 1):
        if i % 2 == 0:
            result.append(left)
            left += 1
        else:
            result.append(right)
            right -= 1
            
    # After satisfying k differences, the remaining elements must be 
    # added in a way that doesn't introduce a new absolute difference.
    # If the last element added was 'left-1' or 'right+1', we continue 
    # the sequence linearly.
    if k % 2 == 0:
        # If k is even, the last element added was 'left-1'.
        # We fill the rest with the remaining 'left' values.
        for i in range(left, right + 1):
            result.append(i)
    else:
        # If k is odd, the last element added was 'right+1'.
        # We fill the rest with the remaining 'right' values in descending order.
        for i in range(right, left - 1, -1):
            result.append(i)
            
    return result
