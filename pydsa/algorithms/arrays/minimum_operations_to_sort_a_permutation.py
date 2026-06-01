METADATA = {
    "id": 3942,
    "name": "Minimum Operations to Sort a Permutation",
    "slug": "minimum-operations-to-sort-a-permutation",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "permutation", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Find the minimum number of operations to sort a permutation by moving elements to any position.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to sort a permutation.
    
    An operation consists of picking any element and moving it to any position.
    To minimize operations, we must find the largest subset of elements that 
    are already in their correct relative sorted order and do not need to be moved.
    For a permutation of 1 to n, this is equivalent to finding the longest 
    subsequence that matches the sorted sequence (1, 2, 3, ...).

    Args:
        nums: A list of integers representing a permutation of 1 to n.

    Returns:
        The minimum number of operations required to sort the list.

    Examples:
        >>> solve([2, 1, 3])
        1
        >>> solve([3, 1, 2])
        2
        >>> solve([1, 2, 3, 4])
        0
    """
    n = len(nums)
    if n <= 1:
        return 0

    # The goal is to find the longest subsequence that follows the pattern 1, 2, 3...
    # because those elements can stay fixed while others are moved around them.
    # Since it's a permutation of 1 to n, we look for the longest subsequence
    # where each element is exactly 1 greater than the previous element in the subsequence.
    
    current_target = 1
    elements_in_place = 0

    for num in nums:
        # If the current number is the next number we need in our 
        # increasing sequence (1, 2, 3...), we "keep" it.
        if num == current_target:
            elements_in_place += 1
            current_target += 1

    # The minimum operations is the total number of elements minus 
    # the number of elements we can leave in their relative positions.
    return n - elements_in_place
