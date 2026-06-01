METADATA = {
    "id": 3489,
    "name": "Zero Array Transformation IV",
    "slug": "zero_array_transformation_iv",
    "category": "Greedy",
    "aliases": [],
    "tags": ["difference_array", "greedy", "array"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(n)",
    "description": "Determine if an array can be transformed into all zeros using a limited number of range operations.",
}

def solve(nums: list[int], queries: list[list[int]]) -> bool:
    """
    Determines if the array 'nums' can be transformed into all zeros using 
    the provided range queries. Each query [l, r] allows subtracting 1 
    from all elements in the range [l, r].

    Args:
        nums: A list of non-negative integers representing the target array.
        queries: A list of integer pairs [l, r] representing the range of indices.

    Returns:
        True if the array can be transformed into all zeros, False otherwise.

    Examples:
        >>> solve([1, 2, 1], [[0, 2], [1, 1]])
        True
        >>> solve([2, 2, 2], [[0, 1]])
        False
    """
    n = len(nums)
    # difference_array tracks the net change applied to each index via range updates.
    # We use a size of n + 1 to handle the boundary condition when updating r + 1.
    difference_array = [0] * (n + 1)

    # Apply each query to the difference array.
    # Incrementing at 'l' and decrementing at 'r + 1' allows us to compute 
    # the total operations applied to any index i using a prefix sum.
    for left, right in queries:
        difference_array[left] += 1
        if right + 1 < n:
            difference_array[right + 1] -= 1

    current_applied_operations = 0
    for i in range(n):
        # The prefix sum of the difference array gives the total number 
        # of queries covering the current index i.
        current_applied_operations += difference_array[i]
        
        # If the number of operations covering index i is less than the 
        # value at nums[i], it is impossible to reduce nums[i] to zero.
        if current_applied_operations < nums[i]:
            return False

    return True
