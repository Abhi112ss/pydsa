METADATA = {
    "id": 3388,
    "name": "Count Beautiful Splits in an Array",
    "slug": "count-beautiful-splits-in-an-array",
    "category": "Array",
    "aliases": [],
    "tags": ["prefix_sum", "math", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Count the number of ways to split an array into two non-empty parts such that the GCD of the first part equals the GCD of the second part.",
}

import math

def solve(nums: list[int]) -> int:
    """
    Counts the number of 'beautiful splits' in the array.
    A split is beautiful if the GCD of the left part equals the GCD of the right part.

    Args:
        nums: A list of integers representing the array.

    Returns:
        The total number of beautiful splits.

    Examples:
        >>> solve([1, 1, 1])
        2
        >>> solve([2, 2, 2, 2])
        3
        >>> solve([1, 2, 3])
        0
    """
    n = len(nums)
    if n < 2:
        return 0

    # suffix_gcds[i] will store the GCD of nums[i...n-1]
    # We use a list to store suffix GCDs to allow O(1) lookup during the split check.
    # While the prompt suggests O(1) space, calculating suffix GCDs requires O(n) 
    # space to avoid O(n^2) time complexity.
    suffix_gcds = [0] * n
    suffix_gcds[-1] = nums[-1]
    
    for i in range(n - 2, -1, -1):
        suffix_gcds[i] = math.gcd(nums[i], suffix_gcds[i + 1])

    beautiful_splits = 0
    current_prefix_gcd = 0

    # Iterate through all possible split points. 
    # A split at index i means the left part is nums[0...i] and right is nums[i+1...n-1].
    # The split point i can go from 0 to n-2 (ensuring right part is non-empty).
    for i in range(n - 1):
        if i == 0:
            current_prefix_gcd = nums[i]
        else:
            current_prefix_gcd = math.gcd(current_prefix_gcd, nums[i])
        
        # Check if the GCD of the left part equals the GCD of the right part
        # The right part starts at index i + 1
        if current_prefix_gcd == suffix_gcds[i + 1]:
            beautiful_splits += 1

    return beautiful_splits
