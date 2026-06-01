METADATA = {
    "id": 3876,
    "name": "Construct Uniform Parity Array II",
    "slug": "construct-uniform-parity-array-ii",
    "category": "Greedy",
    "aliases": [],
    "tags": ["greedy", "arrays"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Construct an array of the same length where all elements have the same parity, minimizing the cost of changes.",
}

def solve(nums: list[int]) -> int:
    """
    Constructs a uniform parity array (all even or all odd) with minimum cost.
    The cost is defined as the sum of absolute differences between original 
    and new elements. However, in the context of parity-only constraints, 
    the cost is typically the count of elements that must be changed to 
    satisfy the parity requirement.

    Args:
        nums: A list of integers.

    Returns:
        The minimum number of elements to change to make all elements 
        have the same parity.

    Examples:
        >>> solve([1, 2, 3, 4])
        2
        >>> solve([2, 4, 6])
        0
        >>> solve([1, 3, 5])
        0
    """
    if not nums:
        return 0

    even_count = 0
    odd_count = 0

    # Count how many numbers are currently even and how many are odd
    for num in nums:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # To make all elements even, we must change all odd elements.
    # To make all elements odd, we must change all even elements.
    # The minimum cost is the minimum of these two operations.
    return min(even_count, odd_count)
