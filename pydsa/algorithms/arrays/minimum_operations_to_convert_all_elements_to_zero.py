METADATA = {
    "id": 3542,
    "name": "Minimum Operations to Convert All Elements to Zero",
    "slug": "minimum-operations-to-convert-all-elements-to-zero",
    "category": "Array",
    "aliases": [],
    "tags": ["greedy", "array_manipulation"],
    "difficulty": "medium",
    "time_complexity": "O(n)",
    "space_complexity": "O(1)",
    "description": "Find the minimum number of operations to make all elements in an array zero using a specific reduction rule.",
}

def solve(nums: list[int]) -> int:
    """
    Calculates the minimum number of operations to convert all elements in the array to zero.
    
    The problem implies a greedy approach where we must address the non-zero elements.
    Based on the standard interpretation of such problems (like reducing elements by 
    a constant or a specific pattern), the minimum operations to clear an array 
    where you can pick a value and subtract it from all occurrences is related 
    to the number of unique non-zero elements.

    Args:
        nums: A list of integers representing the initial state of the array.

    Returns:
        The minimum number of operations required to make all elements zero.

    Examples:
        >>> solve([1, 2, 3, 2, 1])
        3
        >>> solve([0, 0, 0])
        0
        >>> solve([5, 5, 5])
        1
    """
    # Use a set to identify unique non-zero values.
    # Each unique non-zero value represents a necessary operation 
    # if the operation allows reducing all instances of a value by that value.
    unique_non_zeros = set()
    
    for num in nums:
        if num > 0:
            unique_non_zeros.add(num)
            
    # The number of operations is equal to the count of distinct positive integers.
    # This is because in one operation, we can target all instances of the 
    # current smallest positive integer and reduce them to zero.
    return len(unique_non_zeros)
